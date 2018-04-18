# Script generated with Bloom
pkgdesc="ROS - roslang is a common package that all <a href="http://www.ros.org/wiki/Client%20Libraries">ROS client libraries</a> depend on. This is mainly used to find client libraries (via 'rospack depends-on1 roslang')."
url='http://ros.org/wiki/roslang'

pkgname='ros-lunar-roslang'
pkgver='1.14.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
)

depends=('ros-lunar-catkin'
'ros-lunar-genmsg'
)

conflicts=()
replaces=()

_dir=roslang
source=()
md5sums=()

prepare() {
    cp -R $startdir/roslang $srcdir/roslang
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

