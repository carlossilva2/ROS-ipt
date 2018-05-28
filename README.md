# GreenTROS

Projeto Final - Engenharia Informática - 2018

Carlos Silva - 19424

Daniel Cabaceira - 19510

Atualização do GreenT através da implementação de ROS num RaspberryPi e da integração de uma Kinect.

![GreenTROS](Docs/Fotos/greenT.jpg)

## Indice
1. [Instalação](#instalação)
    * [Criar Workspace](#workspace)
    * [Criar Package](#package)
2. [Correr a Package](#iniciar)
3. [Arquitetura em Nós](#arquitetura)

## Instalação

### Workspace

``` bash
source /opt/ros/<distro>/setup.bash
```

``` bash
mkdir -p ~/catkin_ws1/src
```

``` bash
cd ~/catkin_ws1
```

``` bash
catkin_make
```

``` bash
source ~/catkin_ws1/devel/setup.bash
```

``` bash
cd
```

``` bash
echo "source ~/catkin_ws1/devel/setup.bash" >> ~/.bashrc
```

### Package

``` bash
cd ~/catkin_ws1/src
```

``` bash
catkin_create_pkg <nome pkg> geometry_msgs nav_msgs roslib rospy std_msgs tf sensor_msgs cv_bridge
```

* Copiar todos os ficheiros [Python](https://github.com/carlossilva2/GreenT/tree/master/catkin_greent/src/demo_proj/src) para a pasta `~/catkin_ws1/src/<nome pkg>/src`

``` bash
cd ~/catkin_ws1/src/<nome pkg>/src
```

``` bash
chmod +x greenT_joy.py greenT_teleop.py greenT_tf.py greenT_pid_vel.py
```

``` bash
mkdir ~/catkin_ws1/src/<nome pkg>/launch
```

* Copiar o ficheiro [launch](https://github.com/carlossilva2/GreenT/tree/master/catkin_greent/src/demo_proj/launch) para a pasta `~/catkin_ws1/src/<nome pkg>/launch`

* Copiar o ficheiro [packages.xml](https://github.com/carlossilva2/GreenT/blob/master/catkin_greent/src/demo_proj/package.xml) para a pasta `~/catkin_ws1/src/<nome pkg>/`

## Iniciar

``` bash
roslaunch <nome pkg> demo_proj.launch
```

## Arquitetura

![ROS Nodes](Docs/GreenT_Kinect.png)
