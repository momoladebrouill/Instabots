@echo off
set i=0
: l
cd "C:\Users\momol\Desktop\pypi\insta\rand_img"
python main.py
@RD /S /Q "C:\Users\momol\Desktop\pypi\insta\rand_img\config"
@RD /S /Q "C:\Users\momol\Desktop\pypi\insta\rand_img\simple_images"
set /p i=<after.randimg
echo %i%
if %i%==no goto l
pause