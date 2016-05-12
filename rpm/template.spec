Name:           ros-indigo-fzi-icl-can
Version:        1.0.8
Release:        0%{?dist}
Summary:        ROS fzi_icl_can package

Group:          Development/Libraries
License:        LGPLv3
URL:            http://wiki.ros.org/fzi_icl_can
Source0:        %{name}-%{version}.tar.gz

Requires:       kernel-headers
Requires:       popt-devel
Requires:       ros-indigo-catkin
Requires:       ros-indigo-fzi-icl-core
BuildRequires:  cmake
BuildRequires:  popt-devel
BuildRequires:  ros-indigo-fzi-icl-core
BuildRequires:  wget

%description
The fzi_icl_can package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu May 12 2016 heppner <heppner@fzi.de> - 1.0.8-0
- Autogenerated by Bloom

* Wed May 11 2016 heppner <heppner@fzi.de> - 1.0.7-0
- Autogenerated by Bloom

* Wed May 11 2016 heppner <heppner@fzi.de> - 1.0.5-0
- Autogenerated by Bloom

* Wed May 04 2016 heppner <heppner@fzi.de> - 1.0.4-0
- Autogenerated by Bloom

* Mon May 02 2016 heppner <heppner@fzi.de> - 1.0.3-0
- Autogenerated by Bloom

* Mon May 02 2016 heppner <heppner@fzi.de> - 1.0.2-0
- Autogenerated by Bloom

