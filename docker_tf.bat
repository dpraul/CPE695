@ECHO off
SET _dir=/%CD%
SET _dir=%_dir::=%
SET _dir=%_dir:\=/%
@ECHO on
docker run -it -v %_dir%:/notebooks tf python %1 %2 %3 %4