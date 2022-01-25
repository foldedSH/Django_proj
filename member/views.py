from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, redirect
from member.models import UserTable
from argon2 import PasswordHasher # 패스워드 암호화
from argon2.exceptions import VerifyMismatchError


# 회원가입 - 직접 구현
def register(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')

        if UserTable.objects.filter(user_id = user_id).exists():
            return HttpResponse("존재")

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        pw = request.POST.get('pw')
        confirm_pw = request.POST.get('double_pw')
        username = request.POST.get('username')
        email = request.POST.get('email')

        if (user_id=="") or (pw=="") or (confirm_pw=="") or (username=="") or (email==""):
            return 


        # 입력 이메일 형식이 잘못되었거나 이미 존재하는 메일인 경우,
        if UserTable.objects.filter(email = email).exists():
            return HttpResponse("이미 가입된 이메일입니다.")

        # 1차 패스워드와 2차 패스워드가 동일하면 DB 저장
        if pw == confirm_pw:
            m = UserTable(user_id=user_id, pw=PasswordHasher().hash(pw), username=username, email = email)
            m.register_date = timezone.now()
            m.save()

            return redirect('member:login') # 회원가입 성공 후, 메인 페이지로 이동
    
    return render(request, 'member/register.html')


def valid_login(request):
    user_id = request.GET.get('user_id')
    pw = request.GET.get('pw')

    # 회원정보 조회 실패 시 예외 발생
    try:
        corr_pw = UserTable.objects.get(user_id=user_id).pw # 암호화 된 pw

        try:
            if PasswordHasher().verify(corr_pw.encode(), pw.encode()): # 패스워드 확인
                return HttpResponse('Success')

        except VerifyMismatchError as e: # 패스워드 틀린 사용자
            return HttpResponse('Error1')

    except UserTable.DoesNotExist as e: # 없는 사용자
        return HttpResponse('Error2')

    
# 로그인 - 직접 구현
def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        pw = request.POST.get('pw')
        
        corr_pw = UserTable.objects.get(user_id=user_id).pw # 암호화 된 pw
        m = UserTable.objects.get(user_id=user_id, pw=corr_pw)

        request.session['user_id'] = m.user_id
        request.session['username'] = m.username

        return redirect('member:login')
        
    else:
        return render(request, 'member/login.html')


def logout(request):
    del request.session['user_id'] # 개별 삭제
    del request.session['username'] # 개별 삭제
    request.session.flush() # 전체 삭제

    return redirect('member:login') # 메인페이지로 설정

    
def find(request):
    if request.method == 'POST':
        username = request.GET.get('username')
        user_email = request.GET.get('user_email')

        try:
            user_id = UserTable.objects.get(username=username, user_email=user_email).user_id
            find_info = f"{username}님의 ID는 {user_id}입니다."
            return HttpResponse(find_info)

        except UserTable.DoesNotExist as e:
            return HttpResponse('Not Found ID')

    return redirect('member:find')