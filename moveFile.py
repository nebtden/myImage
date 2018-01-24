#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import os.path
import shutil
import subprocess


base_dir = 'E:\Wnmp\html\opencart'
new_base_dir = 'E:\Wnmp\html\opencart\lipapay'


def copyOs(file):
    full_path = os.path.join(base_dir,file)
    is_dir = os.path.isdir(file)
    newfile = os.path.join(new_base_dir,file)
    new_dir  =os.path.dirname(newfile)
    print(new_dir)
    try:
        print('mkdir '+ '' + new_dir)
        out_bytes = subprocess.check_output('mkdir '+ '' + new_dir, shell=True)
    except:
        print('error')
    shutil.copyfile(full_path,newfile)


copyOs(r'admin\controller\extension\payment\lipapay.php')
copyOs(r'catalog\model\extension\payment\lipapay.php')
copyOs(r'catalog\controller\extension\payment\lipapay.php')
copyOs(r'catalog\view\theme\default\template\extension\payment\lipapay.twig')
copyOs(r'admin\controller\extension\payment\lipapay.php')
copyOs(r'admin\view\template\extension\payment\lipapay.twig')
copyOs(r'admin\language\en-gb\extension\payment\lipapay.php')
copyOs(r'admin\view\image\payment\lipapay.png')



# shutil.copy('E:\Wnmp\html\opencart\\admin\controller\extension\payment\lipapay.php',  'E:\Wnmp\html\opencart\lipapay\\admin\controller\extension\payment')
# shutil.copyfile('E:\Wnmp\html\opencart\catalog\model\extension\payment\lipapay.php', 'E:\Wnmp\html\opencart\lipapay\catalog\model\extension\payment\lipapay.php')
#
# shutil.copytree('E:\Wnmp\html\opencart\catalog\controller\extension\payment\lipapay.php','E:\Wnmp\html\opencart\lipapay\catalog\controller\extension\payment\lipapay.php')
# shutil.copytree('E:\Wnmp\html\opencart\catalog\view\theme\default\template\extension\payment\lipapay.twig','E:\Wnmp\html\opencart\lipapay\catalog\view\theme\default\template\extension\payment\lipapay.twig')
# shutil.copytree('E:\Wnmp\html\opencart\admin\controller\extension\payment\lipapay.php','E:\Wnmp\html\opencart\lipapay\admin\controller\extension\payment\lipapay.php')
# shutil.copytree('E:\Wnmp\html\opencart\admin\view\template\extension\payment\lipapay.php','E:\Wnmp\html\opencart\lipapay\admin\view\template\extension\payment\lipapay.php')
# shutil.copytree('E:\Wnmp\html\opencart\admin\language\en-gb\extension\payment\lipapay.php','E:\Wnmp\html\opencart\lipapay\admin\language\en-gb\extension\payment\lipapay.php')

