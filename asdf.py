import bpy
print(bpy.app.version_string)
print('asdf')


# C:\Users\benbe>pip install bpy
# Collecting bpy
#   Using cached bpy-0.0.0a0.tar.gz (19 kB)
# Building wheels for collected packages: bpy
#   Building wheel for bpy (setup.py) ... error
#   ERROR: Command errored out with exit status 1:
#    command: 'c:\users\benbe\appdata\local\programs\python\python36\python.exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\benbe\\AppData\\Local\\Temp\\pip-install-_jc5dyvo\\bpy\\setup.py'"'"'; __file__='"'"'C:\\Users\\benbe\\AppData\\Local\\Temp\\pip-install-_jc5dyvo\\bpy\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d 'C:\Users\benbe\AppData\Local\Temp\pip-wheel-qnkwk73n'
#        cwd: C:\Users\benbe\AppData\Local\Temp\pip-install-_jc5dyvo\bpy\
#   Complete output (56 lines):
#   c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\dist.py:261: UserWarning: Unknown distribution option: 'long_description_content_type'
#     warnings.warn(msg)
#   running bdist_wheel
#   running build
#   running build_py
#   creating build
#   creating build\lib.win-amd64-3.6
#   creating build\lib.win-amd64-3.6\blenderpy
#   copying blenderpy\post_install.py -> build\lib.win-amd64-3.6\blenderpy
#   copying blenderpy\__init__.py -> build\lib.win-amd64-3.6\blenderpy
#   running build_ext
#   Preparing the build environment
#   Searching for compatible Blender online (this will take a while)
#   Found compatible Blender version 2.82
#   Cloning Blender source from git (this will take a while)
#   Cloning precompiled libs from svn (this will take a while)
#   Configuring cmake project and building binaries (this will take a while)
#   Traceback (most recent call last):
#     File "<string>", line 1, in <module>
#     File "C:\Users\benbe\AppData\Local\Temp\pip-install-_jc5dyvo\bpy\setup.py", line 335, in <module>
#       'install_scripts': InstallBlenderScripts
#     File "c:\users\benbe\appdata\local\programs\python\python36\lib\site-packages\setuptools\__init__.py", line 129, in setup
#       return distutils.core.setup(**attrs)
#     File "c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\core.py", line 148, in setup
#       dist.run_commands()
#     File "c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\dist.py", line 955, in run_commands
#       self.run_command(cmd)
#     File "c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\dist.py", line 974, in run_command
#       cmd_obj.run()
#     File "c:\users\benbe\appdata\local\programs\python\python36\lib\site-packages\wheel\bdist_wheel.py", line 223, in run
#       self.run_command('build')
#     File "c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\cmd.py", line 313, in run_command
#       self.distribution.run_command(command)
#     File "c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\dist.py", line 974, in run_command
#       cmd_obj.run()
#     File "c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\command\build.py", line 135, in run
#       self.run_command(cmd_name)
#     File "c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\cmd.py", line 313, in run_command
#       self.distribution.run_command(command)
#     File "c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\dist.py", line 974, in run_command
#       cmd_obj.run()
#     File "C:\Users\benbe\AppData\Local\Temp\pip-install-_jc5dyvo\bpy\setup.py", line 186, in run
#       self.build_cmake(extension)
#     File "C:\Users\benbe\AppData\Local\Temp\pip-install-_jc5dyvo\bpy\setup.py", line 249, in build_cmake
#       build_location= build_path):
#     File "c:\users\benbe\appdata\local\temp\pip-install-_jc5dyvo\bpy\.eggs\bpy_build-1.1.8-py3.6.egg\bpybuild\make.py", line 154, in get_make_commands
#       with_cuda, with_optix, optix_sdk_path) +\
#     File "c:\users\benbe\appdata\local\temp\pip-install-_jc5dyvo\bpy\.eggs\bpy_build-1.1.8-py3.6.egg\bpybuild\make.py", line 49, in get_configure_commands
#       cmakegenerators.get_generators() if
#     File "c:\users\benbe\appdata\local\temp\pip-install-_jc5dyvo\bpy\.eggs\cmake_generators-1.0.8-py3.6.egg\cmakegenerators\__init__.py", line 36, in get_generators
#       r"available on this platform.*:", cmake_help())[-1]
#     File "c:\users\benbe\appdata\local\temp\pip-install-_jc5dyvo\bpy\.eggs\cmake_generators-1.0.8-py3.6.egg\cmakegenerators\__init__.py", line 24, in cmake_help
#       capture_output=True).stdout)
#     File "c:\users\benbe\appdata\local\programs\python\python36\lib\subprocess.py", line 403, in run
#       with Popen(*popenargs, **kwargs) as process:
#   TypeError: __init__() got an unexpected keyword argument 'capture_output'
#   ----------------------------------------
#   ERROR: Failed building wheel for bpy
#   Running setup.py clean for bpy
# Failed to build bpy
# Installing collected packages: bpy
#     Running setup.py install for bpy ... error
#     ERROR: Command errored out with exit status 1:
#      command: 'c:\users\benbe\appdata\local\programs\python\python36\python.exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\benbe\\AppData\\Local\\Temp\\pip-install-_jc5dyvo\\bpy\\setup.py'"'"'; __file__='"'"'C:\\Users\\benbe\\AppData\\Local\\Temp\\pip-install-_jc5dyvo\\bpy\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record 'C:\Users\benbe\AppData\Local\Temp\pip-record-nd2tt3p1\install-record.txt' --single-version-externally-managed --compile --install-headers 'c:\users\benbe\appdata\local\programs\python\python36\Include\bpy'
#          cwd: C:\Users\benbe\AppData\Local\Temp\pip-install-_jc5dyvo\bpy\
#     Complete output (67 lines):
#     c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\dist.py:261: UserWarning: Unknown distribution option: 'long_description_content_type'
#       warnings.warn(msg)
#     running install
#     running build
#     running build_py
#     creating build\lib.win-amd64-3.6
#     creating build\lib.win-amd64-3.6\blenderpy
#     copying blenderpy\post_install.py -> build\lib.win-amd64-3.6\blenderpy
#     copying blenderpy\__init__.py -> build\lib.win-amd64-3.6\blenderpy
#     running build_ext
#     Preparing the build environment
#     Searching for compatible Blender online (this will take a while)
#     Found compatible Blender version 2.82
#     Cloning Blender source from git (this will take a while)
#     Traceback (most recent call last):
#       File "c:\users\benbe\appdata\local\temp\pip-install-_jc5dyvo\bpy\.eggs\bpy_build-1.1.8-py3.6.egg\bpybuild\sources.py", line 196, in checkout
#         repo = GitRepo(str(full_path))
#       File "c:\users\benbe\appdata\local\temp\pip-install-_jc5dyvo\bpy\.eggs\gitpython-3.1.2-py3.6.egg\git\repo\base.py", line 181, in __init__
#         raise InvalidGitRepositoryError(epath)
#     git.exc.InvalidGitRepositoryError: C:\Users\benbe\AppData\Local\Temp\pip-install-_jc5dyvo\bpy\build\temp.win-amd64-3.6\Release\blender

#     During handling of the above exception, another exception occurred:

#     Traceback (most recent call last):
#       File "<string>", line 1, in <module>
#       File "C:\Users\benbe\AppData\Local\Temp\pip-install-_jc5dyvo\bpy\setup.py", line 335, in <module>
#         'install_scripts': InstallBlenderScripts
#       File "c:\users\benbe\appdata\local\programs\python\python36\lib\site-packages\setuptools\__init__.py", line 129, in setup
#         return distutils.core.setup(**attrs)
#       File "c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\core.py", line 148, in setup
#         dist.run_commands()
#       File "c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\dist.py", line 955, in run_commands
#         self.run_command(cmd)
#       File "c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\dist.py", line 974, in run_command
#         cmd_obj.run()
#       File "c:\users\benbe\appdata\local\programs\python\python36\lib\site-packages\setuptools\command\install.py", line 61, in run
#         return orig.install.run(self)
#       File "c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\command\install.py", line 545, in run
#         self.run_command('build')
#       File "c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\cmd.py", line 313, in run_command
#         self.distribution.run_command(command)
#       File "c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\dist.py", line 974, in run_command
#         cmd_obj.run()
#       File "c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\command\build.py", line 135, in run
#         self.run_command(cmd_name)
#       File "c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\cmd.py", line 313, in run_command
#         self.distribution.run_command(command)
#       File "c:\users\benbe\appdata\local\programs\python\python36\lib\distutils\dist.py", line 974, in run_command
#         cmd_obj.run()
#       File "C:\Users\benbe\AppData\Local\Temp\pip-install-_jc5dyvo\bpy\setup.py", line 186, in run
#         self.build_cmake(extension)
#       File "C:\Users\benbe\AppData\Local\Temp\pip-install-_jc5dyvo\bpy\setup.py", line 233, in build_cmake
#         git_repo.checkout(blender_path) # Clones into 'blender'
#       File "c:\users\benbe\appdata\local\temp\pip-install-_jc5dyvo\bpy\.eggs\bpy_build-1.1.8-py3.6.egg\bpybuild\sources.py", line 200, in checkout
#         GitRepo.clone_from(self.BASE_URL, str(full_path))
#       File "c:\users\benbe\appdata\local\temp\pip-install-_jc5dyvo\bpy\.eggs\gitpython-3.1.2-py3.6.egg\git\repo\base.py", line 1019, in clone_from
#         return cls._clone(git, url, to_path, GitCmdObjectDB, progress, multi_options, **kwargs)
#       File "c:\users\benbe\appdata\local\temp\pip-install-_jc5dyvo\bpy\.eggs\gitpython-3.1.2-py3.6.egg\git\repo\base.py", line 960, in _clone
#         finalize_process(proc, stderr=stderr)
#       File "c:\users\benbe\appdata\local\temp\pip-install-_jc5dyvo\bpy\.eggs\gitpython-3.1.2-py3.6.egg\git\util.py", line 328, in finalize_process
#         proc.wait(**kwargs)
#       File "c:\users\benbe\appdata\local\temp\pip-install-_jc5dyvo\bpy\.eggs\gitpython-3.1.2-py3.6.egg\git\cmd.py", line 408, in wait
#         raise GitCommandError(self.args, status, errstr)
#     git.exc.GitCommandError: Cmd('git') failed due to: exit code(128)
#       cmdline: git clone -v git://git.blender.org/blender.git build\temp.win-amd64-3.6\Release\blender
#       stderr: 'fatal: destination path 'build\temp.win-amd64-3.6\Release\blender' already exists and is not an empty directory.
#     '
#     ----------------------------------------
# ERROR: Command errored out with exit status 1: 'c:\users\benbe\appdata\local\programs\python\python36\python.exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\benbe\\AppData\\Local\\Temp\\pip-install-_jc5dyvo\\bpy\\setup.py'"'"'; __file__='"'"'C:\\Users\\benbe\\AppData\\Local\\Temp\\pip-install-_jc5dyvo\\bpy\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record 'C:\Users\benbe\AppData\Local\Temp\pip-record-nd2tt3p1\install-record.txt' --single-version-externally-managed --compile --install-headers 'c:\users\benbe\appdata\local\programs\python\python36\Include\bpy' Check the logs for full command output