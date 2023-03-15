import tempfile
import os
import glob
import maya.cmds as mc
import sys

def savepb():
    sys.path.append( '/Users/*/maya/Scripts' )
    # folder destinasi, source dan nama format file blast pertama
    src_folder = r"C:/ProjectA/EP00/blast/"
    dst_folder = r"C:/ProjectA/EP00/blast/archive"
    file_name = "EP00_SH00.mov"

    ## cek apakah file EP00_SH00.mov sudah ada
    ## jika sudah ada maka buat save file baru di archive dengan penomoran seri EP00_SH00_v0x.mov
    if os.path.exists(src_folder + file_name):
            
        cekDulu = os.path.join(dst_folder, "EP00_SH00_v01.mov")
            
        if not os.path.isfile(cekDulu) :
            mc.sysFile("C:/ProjectA/EP00/blast/archive", makeDir=True)
            destWindows = os.path.join( dst_folder, "EP00_SH00_v00.mov" )
            srcWindows = os.path.join( src_folder, file_name )
            mc.sysFile( srcWindows, copy=destWindows )
            
        ## mengecek file terbaru di folder target
        list_of_files = glob.glob('C:/ProjectA/EP00/blast/archive/*')
        latest_file = max(list_of_files, key=os.path.getctime)
                
        # mengambil file yang terbaru
        stringObj = latest_file

        # memisahkan folder dengan file dan ambil nama filenya saja 
        lastElement = stringObj.split('/')[-1]

        # mengambil serinya
        ambilVersi = lastElement.split("_")
        ambilVersi.reverse()
                    
        targetPotong = ambilVersi[0]
        b = targetPotong.split(".")

        ambilSeri = b[0]

        # memisahkan karakter v dengan angka versi
        angkaSeri = ambilSeri.split("v")
        seriTambah = int(angkaSeri[1])
        seriBerikutnya = seriTambah + 1
        seriStr = str(seriBerikutnya)
            
        # pemrosesan seri selanjutnya dari seri file terbaru
        if not seriTambah < 9 :
            existsFileName = os.path.join("EP00_SH00_v"+ seriStr +".mov")
        else :
            existsFileName = os.path.join("EP00_SH00_v0"+ seriStr +".mov")
            
        ## Cek file terbaru, kalau sudah ada save file dengan seri selanjutnya
        if not os.path.isfile(existsFileName) :

            cekV01 = os.path.join(dst_folder, "EP00_SH00_v00.mov")

            if os.path.isfile(cekV01) :
                mc.sysFile("C:/ProjectA/EP00/blast/archive/EP00_SH00_v00.mov", delete=True)

            # copy file sebelumnya ke archive
            destWindows = os.path.join( dst_folder, existsFileName )
            srcWindows = os.path.join( src_folder, file_name )
            mc.sysFile( srcWindows, copy=destWindows )

            a = os.path.join(src_folder,file_name)
            movie_path = mc.playblast(format="qt", sqt=0, cc=1, v=1, orn=1, fp=4, percent=100, compression="H.264", quality=70, w=1280, h=720, filename=a, fo=True)
                
            print(movie_path)
                
        ## Cek file terbaru, kalau belum ada, buat folder archive dan save file dengan seri baru v01
        else :

            cekV01 = os.path.join(dst_folder, "EP00_SH00_v00.mov")

            if os.path.isfile(cekV01) :
                mc.sysFile("C:/ProjectA/EP00/blast/archive/EP00_SH00_v00.mov", delete=True)

            # copy file sebelumnya ke archive
            srcWindows = os.path.join( src_folder, file_name )
            destWindows = os.path.join( dst_folder, "EP00_SH00_v01.mov" )
            mc.sysFile( srcWindows, copy=destWindows )
                
            a = os.path.join(src_folder,file_name)
            movie_path = mc.playblast(format="qt", sqt=0, cc=1, v=1, orn=1, fp=4, percent=100, compression="H.264", quality=70, w=1280, h=720, filename=a, fo=True)
                
            print(movie_path)

    ## save file baru di folder scene
    else :
        a = os.path.join(src_folder,file_name)
        movie_path = mc.playblast(format="qt", sqt=0, cc=1, v=1, orn=1, fp=4, percent=100, compression="H.264", quality=70, w=1280, h=720,filename=a, fo=True)
            
        print(movie_path)

savepb()