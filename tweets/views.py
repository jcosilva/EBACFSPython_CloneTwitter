from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.db.models import Q
from .models import Tweet, Like, Follow
from .forms import TweetForm

User = get_user_model()

@login_required
def home(request):
    # Obtém IDs dos usuários que o usuário atual segue
    following_users = Follow.objects.filter(user=request.user).values_list('followed_user', flat=True)
    # Obtém tweets do usuário atual e dos usuários que ele segue
    tweets = Tweet.objects.filter(
        Q(user=request.user) | Q(user__in=following_users)
    ).order_by('-created_at')
    # Obtém IDs dos tweets que o usuário atual deu like
    liked_tweet_ids = Like.objects.filter(user=request.user).values_list('tweet_id', flat=True)
    context = {
        'tweets': tweets,
        'liked_tweet_ids': liked_tweet_ids
    }
    return render(request, 'tweets/home.html', context)

@login_required
def create_tweet(request):
    print("User:", request.user)  # Verificar se o usuário está autenticado
    print("User is authenticated:", request.user.is_authenticated)  # Verificar status de autenticação
    if request.method == 'POST':
        form = TweetForm(request.POST)
        print("Form data:", request.POST)  # Ver os dados do formulário
        if form.is_valid():
            print("Form is valid")  # Confirmar que o formulário é válido
            tweet = form.save(commit=False)
            print("Tweet before user:", tweet.__dict__)  # Ver o objeto tweet antes de adicionar o usuário
            tweet.user = request.user
            print("Tweet after user:", tweet.__dict__)  # Ver o objeto tweet depois de adicionar o usuário
            tweet.save()
            return redirect('home')
        else:
            print("Form errors:", form.errors)  # Ver erros do formulário se houver
    else:
        form = TweetForm()
    return render(request, 'tweets/create_tweet.html', {'form': form})

@login_required
def like_tweet(request, id):
    tweet = get_object_or_404(Tweet, id=id)
    like = Like.objects.filter(user=request.user, tweet=tweet).first()
    if like:
        # Se já existe um like, remove
        like.delete()
    else:
        # Se não existe, cria um novo like
        Like.objects.create(user=request.user, tweet=tweet)
    return redirect('home')

@login_required
def delete_tweet(request, id):
    tweet = get_object_or_404(Tweet, id=id)
    if tweet.user == request.user:  # Garante que só o dono pode deletar
        tweet.delete()
    return redirect('home')

@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    # Verifica se não está tentando seguir a si mesmo
    if request.user != user_to_follow:
        # Cria a relação de seguir se não existir
        Follow.objects.get_or_create(user=request.user, followed_user=user_to_follow)
    # Redireciona para o perfil ou de volta para os resultados da pesquisa
    referer = request.META.get('HTTP_REFERER')
    if referer and 'search' in referer:
        return redirect('search_users')
    return redirect('profile', user_id=user_id)

@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    # Remove a relação de seguir
    Follow.objects.filter(user=request.user, followed_user=user_to_unfollow).delete()
    # Redireciona para o perfil ou de volta para os resultados da pesquisa
    referer = request.META.get('HTTP_REFERER')
    if referer and 'search' in referer:
        return redirect('search_users')
    return redirect('profile', user_id=user_id)

@login_required
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    tweets = Tweet.objects.filter(user=user).order_by('-created_at')
    is_following = Follow.objects.filter(user=request.user, followed_user=user).exists()
    # Obtém IDs dos tweets que o usuário atual deu like
    liked_tweet_ids = Like.objects.filter(user=request.user).values_list('tweet_id', flat=True)
    context = {
        'profile_user': user,
        'tweets': tweets,
        'is_following': is_following,
        'followers_count': user.followers.count(),
        'following_count': user.following.count(),
        'liked_tweet_ids': liked_tweet_ids,
    }
    return render(request, 'tweets/profile.html', context)

@login_required
def search_users(request):
    query = request.GET.get('q', '')
    users = []
    following_ids = []
    if query:
        # Modifique esta linha para buscar apenas pelo email
        users = User.objects.filter(
            email__icontains=query
        ).exclude(id=request.user.id)
        # Obtém lista de IDs dos usuários que o usuário atual já segue
        following_ids = Follow.objects.filter(
            user=request.user
        ).values_list('followed_user_id', flat=True)
    context = {
        'users': users,
        'query': query,
        'following_ids': following_ids,
    }
    return render(request, 'tweets/search_results.html', context)
