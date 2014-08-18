Name:           ros-indigo-mk
Version:        1.11.5
Release:        0%{?dist}
Summary:        ROS mk package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ROS
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-rosbuild
BuildRequires:  ros-indigo-catkin >= 0.5.69

%description
A collection of .mk include files for building ROS architectural elements. Most
package authors should use cmake .mk, which calls CMake for the build of the
package. The other files in this package are intended for use in exotic
situations that mostly arise when importing 3rdparty code.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Aug 18 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.5-0
- Autogenerated by Bloom

