import os
import natsort # 정렬관련 외부 라이브러리(현재 폴더에 있는 파일 순서유지를 위해 필요) / library that is used to sort list

#함수 선언 / Define function
def change_name(folder, format):
    namelist = os.listdir(folder)  #os.listdir은 경로에 있는 파일명을 리스트로 반환 / os.listdir returns list of filenames in path
    namelist = natsort.natsorted(namelist,alg=natsort.LOCALE)  #alg=natsort.LOCALE은 해당 폴더 정렬법과 같게 정렬하라는 뜻 / alg=natsort.LOCALE means sort namelist same way as your folder
    i = 1
    for filename in namelist:
        #이미지 파일만 변환할 것이므로 확장자 추가 / I would like to change only image files so add some extensions
        if (filename[-3:] != "png") and (filename[-3:] != "PNG" ) and (filename[-3:] != "jpg") and (filename[-3:] != "JPG") :
            i += 1
            continue
           
        # os.rename(A,B) : A path를  B path 로 바꾼다. / os.rename(A,B) : Change path A to path B
        # zfill(4): 숫자는 4자리로 zerofill 하였다.
        os.rename(folder+filename,folder+format+str(i).zfill(4)+".jpg")

        i += 1
    
    print("%d 개 변환됨"%i)

# folder: 변환할 파일들이 있는 폴더, format: 숫자 앞에 붙을 파일명 / folder: Folder that has files to be changed, format: Name that attached before number
folder = "C:\\Users\\Admin\\Pictures\\AmericaTour\\"

change_name(folder,"18USA")
