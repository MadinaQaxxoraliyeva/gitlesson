"""Git va gitHub haqida"""
# Git nima???
"""Git ==>> Version Control System (VCS) yani versiyalarni boshqarish tizimi 
"""
# Masalan:
"""
1 Bir loyihaning nomi ;
2 Bir loyihaning nomi: yangilangan; 
3 Bir loyihaning nomi: yana yangilangan; 
4 Bir loyihaning nomi: oxirgi yangilangan;
"""
# Gitning afzalliklari:
"""
1. Kod versiyasini nazorat qilish
2. Qanday o'zgartirishlar kiritinganligi haqida ma'lumot beradi
3. O'zgartirish kiritilgan kodga kim tomonidan va qachon va aynan kim tomonidan kiritilganligi haqida 
ma'lumot beradi
4. Loyihalar bn ishlashda indivudial va jamoviy ishlash imkoniyatini beradi
5. Git for marketing / product management / designers / custom support / human resourses/...;
"""
# Git va GitHub farqi?
"""
git - local - Version Control System
githab - online - Version Control System Hosting Service (Xizmati)
"""
# git dasturini o'rnatish:
"""
Windows - Git Bash
MacOs - Terminal, iTerm, Kitty;
   Git Bash linux tizimini windowsda ishlashiga yordam beradi
   Ushbu dastur Linux terminalining funksional xususiyatlarini o'zida integratsiyalashgan
"""
# Git sozlab olish
"""
1. git config... = gitni sozlab olish un ishlatiladigan buyruq
2. git congif --list = barcha sozlamalarni ko'rsatish
3. git config user.name = git foydalanuvchisining ismini korish
4. git config user.email = git foydalanuvchisining emailini korish


Agar bular sozlanmagan bo'lsa sozlab olamiz:
   1. git config -global user.name "foydalanuvchi ismi" ==>> foydalanuvchi ismini qo'yish
   2. git config -global user.email "foydalanuvchi emaili" ==>> foydalanuvchi emailini qo'yish
   
   3. git config --global --unset user.name "foydalanuvchi eski ismi" ==>> eski  foydalanuvchi ismini o'chirish 
   4. git config --global user.name "yangi foydalanuvchi ismi" ==>> yangi foydalanuvchi ismi qo'yish
"""
#  Terminal oynasi to'lin ketganda git bash da  ' Ctrl+l ' tugmaarini bosishimiz mumkin
# Gitda yangi loyiha yaratish
"""
1. repository - (repos qisqartmasi ) ombor loyiha 
2. git init - yangi git loyihalarini boshlash un ishlatiladi. Loyiha ichida faqat bir marta ishlating 
3. git status - o'zgarishga uchragan holatni tekshirish
  ** touch - biron fayl yaratish un ishlatamiz "faylnomi.faylqisqartmasi" va uning sanasini yangilsh un 
  ishlatilamiz bu buyruq 'file.txt' nomli fayli yaratadi yoki agar bunday fayl bo'lsa uning sanasini yangilaydi.
  ** mkdir papka nomi - papka yaratish
  ** rm fayl.nomi - fayl o'chirish
  **** echo 'yoziladigan matn' >> faylnomi.formati ==>> fayl ochib shu fayl ichiga ma'lumotni yozib beradi 
4. git add ... - loyihadagi yangi fayllar, o'zgarishlar va o'chirishlarni xotiraga navbatga olish un qo'yiladi
git add  faylnomi
5. git add . - barcha o'zgarish o'chirilish va qo'shilish
6. -A vs --all -  barcha o'zgarish o'chirilish va qo'shilish
7. --command - flag deyiladi
"""

"""
   git commit ... ==>> navbatga qo'yilgan fayllarning butunlay saqlash un va xotiraga saqlanayotganida ham 
   xabar bn saqlash imkonini beradi (xabar bn qilishimiz kk)
1. git commit -m "xabar nomi" ==>> xabarimizni yozib saqlaymiz
2. git commit -amend -m 'xabar' ==>> Bu jarayonda --amend buyruq avalgi commintni yangilab , yangi o'zgarishlar bn 
yangi commitni qo'shadi .Avvalgi commit o'zgartiriladi va yangi bir commit tarixi yaratiladi yani eski commit o'chib ketadi
3. git log ==>> shu paytgacha commitlar tarixini ko'rish
4. git log --pretty ==>> yuqoridagi git log  bn bir xil
5. git commit -a -m "xabar" ==>> o'zgartirishni navbatga olmasdan yani git add . qilmasdan commit yaratish
  ** code . ==>> ushbu turgan faylimizni kod editorda ochish un (VS code)
  ** start . ==>> ushbu commidline orqali turgan faylimizni ichiga kirish
"""
# Fayldagi o'zgarishlarni bekor qilish
"""
1. git checkout --faylnomi ==>> shu fayldagi o'zgarishlarni bekor qiladi
2. git checkout maxsus kod ==>> loyihamizning istalgan versiyasiga o'tish
3. git checkout master ==>> oxirgi versiyaga qaytish
 Bu faqat o'zgarishlarni git add . qilishdan avval bekor qilyapmiz
"""
# git add dagi navbatni bekor qilish
"""
1. git reset faylnomi;
2. git reset. ==>> barcha o'zgarishlarni navbatdan olish
"""

# Branch \ Merge
"""
1. branch - filial
2. Merge - biriktirish bu bir nechta 'branch'larni biriktirish un ishlatiladi
"""
# Branch yaratish
"""
1. git branch ==>> hozirgi mavjud branchlarni royxatini ko'rish
2. git branchnomi ==>> yangi branch yaratish
3. git checkout nomi ==>> berilgan branchga o'tish
4. git merge branchnomi ==>> berilgan brenchni mavjud branch yuklash
*** git rm faylnomi ==>> git reposdagi barcha fayllarni o'chirish
***git commit -m "barcha fayllarni o'chirish" ==>> shunda local fayllar ham o'chadi
*** git push origin master ==>> reposni serverga yuklavorsak u yerda ham shunday bo'ladi
5. git branch -M yangi_branch_nomi ==>> branch nomini almashtirish
6. git branch -D branch_nomi ==>> branchni o'chirish un
"""