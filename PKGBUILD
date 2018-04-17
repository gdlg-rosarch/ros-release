# Script generated with Bloom
pkgdesc="ROS - ROS packaging system"
url='http://www.ros.org/wiki/ROS'

pkgname='ros-lunar-ros'
pkgver='1.14.2'_'1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
)

depends=('ros-lunar-catkin'
'ros-lunar-mk'
'ros-lunar-rosbash'
'ros-lunar-rosboost-cfg'
'ros-lunar-rosbuild'
'ros-lunar-rosclean'
'ros-lunar-roscreate'
'ros-lunar-roslang'
'ros-lunar-roslib'
'ros-lunar-rosmake'
'ros-lunar-rosunit'
)

conflicts=()
replaces=()

_dir=ros
source=()
md5sums=()

prepare() {
    cp -R $startdir/ros $srcdir/ros
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

