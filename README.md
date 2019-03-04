# Intel 8080 Assembler
<dl>
  <br>
  <dd> Project wrapper online <a href="http://sensi.org/~svo/i8080/">sensi intel 8080 assembler</a>. It compiles your asm files and save .com files to your working directory automatically in local. </dd>
</dl>

<dl>
  <dd>
<div align="center" >
    <img src="/assets/Screenshot from 2019-03-04 23-07-30.png" </img> 
</div>
 </dd>   
 <dd>
   <dd>
<div align="center">
    <img src="/assets/Screenshot from 2019-03-04 23-08-57.png" </img> 
</div>
     </dd>
    </dd>
</dl>

## Usage
<dl>
  <br>
  <dd>It has simple usage.You can use from ternimal or sublime text editor.</dd>
</dl>

<ul>
  
<dl>
    <dd>- If you copy executable file /usr/local/bin , you can use program like ls,cd,pwd etc.</dd>
    <dd>

      ~$ i8080Builder file.asm 
   </dd>
</dl>

</ul>

<ul>
  
<dl>

  <dd>- If you put program in your working directory, you can run like executable.</dd>
    <dd>

      ~$ ./i8080Builder file.asm 
   </dd>
</dl>

</ul>

<ul>
<dl>

  <dd>- If you use sublime text editor, you use sublime build option.</dd>
    <dd>
      
      Select Tools > Build System > i8080Build
      Then use Ctrl + b shortcut
   </dd>
</dl>

</ul>

## Prequest

<dl>
  <dd>Program developed and tested in linux system. So </dd>
</dl>
  
<ul>  
<dl>
  
  <dd>- Computer must be 64 bit system and linux. </dd>
  <dd>- Python 3 must be installed.</dd>
  <dd>- Python 3 pip pakage installer </dd>
  <dd>- Firefox web browser </dd>
</dl>
</ul>



## Installation

<dl>
  <dd>You can use buil.sh for installing (recomended) or you can follow step by step instruction. Please make sure all dependency installed perfectly. </dd>
</dl>

<ul>
<dl>
    <dd>- If you want to use sublime build options, you create new build sytem and copy the script or copy the i8080Build.sublime-build            correct location.
          Hint: Tools > Build System > New Build Sytem  </dd>
    <dd>
      
      {
          "shell_cmd": "i8080Builder \"$file_name\"",
          "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
          "selector": "source.asm"
      }
   </dd>
</dl>
</ul>

<ul>
<dl>
    <dd>- With using buil.sh. Script install all dependencies and move executable correct directory one at a time. </dd>
    <dd>
      
      ~$ cd /archived_directory
      ~$ chmod +x build.sh  
      ~$ ./build.sh 
   </dd>
</dl>
</ul>

<ul>
<dl>
  <dd>- Step by step instruction. </dd>
</dl>

<ul>
<dl>
    <dd>- Uptade your firefox for running.</dd>
    <dd>
      
      ~$ sudo apt-get install firefox
   </dd>
</dl>
</ul>

<ul>
<dl>
    <dd>- Move local web page file to /usr/local/bin</dd>
    <dd>
      
      ~$ sudo mv i8080AssemblerSensi/ /usr/local/bin/
   </dd>
</dl>
</ul>


<ul>
<dl>
    <dd>- Give execution perimssion and move files to /usr/local/bin</dd>
    <dd>
      
      ~$ chmod 777 i8080Builder.py
      ~$ sudo mv i8080Builder.py i8080Builder
      ~$ sudo mv i8080Builder /usr/local/bin/
   </dd>
</dl>
</ul>


<ul>
<dl>
    <dd>- Give execution perimssion geckodriver and move file to /usr/local/bin . Geckodriver for using firefox webdriver.</dd>
    <dd>
      
      ~$ chmod +x geckodriver
      ~$ sudo mv geckodriver /usr/local/bin/
   </dd>
</dl>
</ul>


<ul>
<dl>
    <dd>- If you have not pip packet installer, install pip </dd>
    <dd>
      
      ~$ sudo apt-get install python3-pip
   </dd>
</dl>
</ul>


<ul>
<dl>
    <dd>- Intstall selenium framework with pip pakage installer</dd>
    <dd>
      
      ~$ sudo python3 -m pip install selenium
   </dd>
</dl>
</ul>
</ul>

## Thanks
<dl>
  <dd> Great thanks to sensi.org and selenium contributor.</dd>
</dl>




