#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtsensors
Version  : 5.12.0
Release  : 13
URL      : https://download.qt.io/official_releases/qt/5.12/5.12.0/submodules/qtsensors-everywhere-src-5.12.0.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.12/5.12.0/submodules/qtsensors-everywhere-src-5.12.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qtsensors-lib = %{version}-%{release}
Requires: qtsensors-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : pkgconfig(Qt5Bluetooth)
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5DBus)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(Qt5Xml)

%description
No detailed description available

%package dev
Summary: dev components for the qtsensors package.
Group: Development
Requires: qtsensors-lib = %{version}-%{release}
Provides: qtsensors-devel = %{version}-%{release}

%description dev
dev components for the qtsensors package.


%package lib
Summary: lib components for the qtsensors package.
Group: Libraries
Requires: qtsensors-license = %{version}-%{release}

%description lib
lib components for the qtsensors package.


%package license
Summary: license components for the qtsensors package.
Group: Default

%description license
license components for the qtsensors package.


%prep
%setup -q -n qtsensors-everywhere-src-5.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
%qmake
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1544049247
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtsensors
cp LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtsensors/LICENSE.FDL
cp LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtsensors/LICENSE.GPL2
cp LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtsensors/LICENSE.GPL3
cp LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtsensors/LICENSE.GPL3-EXCEPT
cp LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtsensors/LICENSE.LGPL3
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qaccelerometer_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qaltimeter_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qambientlightsensor_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qambienttemperaturesensor_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qcompass_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qdistancesensor_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qgyroscope_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qholstersensor_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qhumiditysensor_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qirproximitysensor_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qlidsensor_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qlightsensor_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qmagnetometer_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qorientationsensor_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qpressuresensor_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qproximitysensor_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qrotationsensor_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qsensor_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qsensorbackend_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qsensorgesture_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qsensorgesturemanagerprivate_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qtapsensor_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qtiltsensor_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/qtsensors-config_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/sensorlog_p.h
/usr/include/qt5/QtSensors/5.12.0/QtSensors/private/simulatorgesturescommon_p.h
/usr/include/qt5/QtSensors/QAccelerometer
/usr/include/qt5/QtSensors/QAccelerometerFilter
/usr/include/qt5/QtSensors/QAccelerometerReading
/usr/include/qt5/QtSensors/QAltimeter
/usr/include/qt5/QtSensors/QAltimeterFilter
/usr/include/qt5/QtSensors/QAltimeterReading
/usr/include/qt5/QtSensors/QAmbientLightFilter
/usr/include/qt5/QtSensors/QAmbientLightReading
/usr/include/qt5/QtSensors/QAmbientLightSensor
/usr/include/qt5/QtSensors/QAmbientTemperatureFilter
/usr/include/qt5/QtSensors/QAmbientTemperatureReading
/usr/include/qt5/QtSensors/QAmbientTemperatureSensor
/usr/include/qt5/QtSensors/QCompass
/usr/include/qt5/QtSensors/QCompassFilter
/usr/include/qt5/QtSensors/QCompassReading
/usr/include/qt5/QtSensors/QDistanceFilter
/usr/include/qt5/QtSensors/QDistanceReading
/usr/include/qt5/QtSensors/QDistanceSensor
/usr/include/qt5/QtSensors/QGyroscope
/usr/include/qt5/QtSensors/QGyroscopeFilter
/usr/include/qt5/QtSensors/QGyroscopeReading
/usr/include/qt5/QtSensors/QHolsterFilter
/usr/include/qt5/QtSensors/QHolsterReading
/usr/include/qt5/QtSensors/QHolsterSensor
/usr/include/qt5/QtSensors/QHumidityFilter
/usr/include/qt5/QtSensors/QHumidityReading
/usr/include/qt5/QtSensors/QHumiditySensor
/usr/include/qt5/QtSensors/QIRProximityFilter
/usr/include/qt5/QtSensors/QIRProximityReading
/usr/include/qt5/QtSensors/QIRProximitySensor
/usr/include/qt5/QtSensors/QLidFilter
/usr/include/qt5/QtSensors/QLidReading
/usr/include/qt5/QtSensors/QLidSensor
/usr/include/qt5/QtSensors/QLightFilter
/usr/include/qt5/QtSensors/QLightReading
/usr/include/qt5/QtSensors/QLightSensor
/usr/include/qt5/QtSensors/QMagnetometer
/usr/include/qt5/QtSensors/QMagnetometerFilter
/usr/include/qt5/QtSensors/QMagnetometerReading
/usr/include/qt5/QtSensors/QOrientationFilter
/usr/include/qt5/QtSensors/QOrientationReading
/usr/include/qt5/QtSensors/QOrientationSensor
/usr/include/qt5/QtSensors/QPressureFilter
/usr/include/qt5/QtSensors/QPressureReading
/usr/include/qt5/QtSensors/QPressureSensor
/usr/include/qt5/QtSensors/QProximityFilter
/usr/include/qt5/QtSensors/QProximityReading
/usr/include/qt5/QtSensors/QProximitySensor
/usr/include/qt5/QtSensors/QRotationFilter
/usr/include/qt5/QtSensors/QRotationReading
/usr/include/qt5/QtSensors/QRotationSensor
/usr/include/qt5/QtSensors/QSensor
/usr/include/qt5/QtSensors/QSensorBackend
/usr/include/qt5/QtSensors/QSensorBackendFactory
/usr/include/qt5/QtSensors/QSensorChangesInterface
/usr/include/qt5/QtSensors/QSensorFilter
/usr/include/qt5/QtSensors/QSensorGesture
/usr/include/qt5/QtSensors/QSensorGestureManager
/usr/include/qt5/QtSensors/QSensorGesturePluginInterface
/usr/include/qt5/QtSensors/QSensorGestureRecognizer
/usr/include/qt5/QtSensors/QSensorManager
/usr/include/qt5/QtSensors/QSensorPluginInterface
/usr/include/qt5/QtSensors/QSensorReading
/usr/include/qt5/QtSensors/QTapFilter
/usr/include/qt5/QtSensors/QTapReading
/usr/include/qt5/QtSensors/QTapSensor
/usr/include/qt5/QtSensors/QTiltFilter
/usr/include/qt5/QtSensors/QTiltReading
/usr/include/qt5/QtSensors/QTiltSensor
/usr/include/qt5/QtSensors/QtSensors
/usr/include/qt5/QtSensors/QtSensorsDepends
/usr/include/qt5/QtSensors/QtSensorsVersion
/usr/include/qt5/QtSensors/qaccelerometer.h
/usr/include/qt5/QtSensors/qaltimeter.h
/usr/include/qt5/QtSensors/qambientlightsensor.h
/usr/include/qt5/QtSensors/qambienttemperaturesensor.h
/usr/include/qt5/QtSensors/qcompass.h
/usr/include/qt5/QtSensors/qdistancesensor.h
/usr/include/qt5/QtSensors/qgyroscope.h
/usr/include/qt5/QtSensors/qholstersensor.h
/usr/include/qt5/QtSensors/qhumiditysensor.h
/usr/include/qt5/QtSensors/qirproximitysensor.h
/usr/include/qt5/QtSensors/qlidsensor.h
/usr/include/qt5/QtSensors/qlightsensor.h
/usr/include/qt5/QtSensors/qmagnetometer.h
/usr/include/qt5/QtSensors/qorientationsensor.h
/usr/include/qt5/QtSensors/qpressuresensor.h
/usr/include/qt5/QtSensors/qproximitysensor.h
/usr/include/qt5/QtSensors/qrotationsensor.h
/usr/include/qt5/QtSensors/qsensor.h
/usr/include/qt5/QtSensors/qsensorbackend.h
/usr/include/qt5/QtSensors/qsensorgesture.h
/usr/include/qt5/QtSensors/qsensorgesturemanager.h
/usr/include/qt5/QtSensors/qsensorgestureplugininterface.h
/usr/include/qt5/QtSensors/qsensorgesturerecognizer.h
/usr/include/qt5/QtSensors/qsensormanager.h
/usr/include/qt5/QtSensors/qsensorplugin.h
/usr/include/qt5/QtSensors/qsensorsglobal.h
/usr/include/qt5/QtSensors/qtapsensor.h
/usr/include/qt5/QtSensors/qtiltsensor.h
/usr/include/qt5/QtSensors/qtsensors-config.h
/usr/include/qt5/QtSensors/qtsensorsversion.h
/usr/lib64/cmake/Qt5Sensors/Qt5SensorsConfig.cmake
/usr/lib64/cmake/Qt5Sensors/Qt5SensorsConfigVersion.cmake
/usr/lib64/cmake/Qt5Sensors/Qt5Sensors_IIOSensorProxySensorPlugin.cmake
/usr/lib64/cmake/Qt5Sensors/Qt5Sensors_LinuxSensorPlugin.cmake
/usr/lib64/cmake/Qt5Sensors/Qt5Sensors_QShakeSensorGesturePlugin.cmake
/usr/lib64/cmake/Qt5Sensors/Qt5Sensors_QtSensorGesturePlugin.cmake
/usr/lib64/cmake/Qt5Sensors/Qt5Sensors_genericSensorPlugin.cmake
/usr/lib64/libQt5Sensors.prl
/usr/lib64/libQt5Sensors.so
/usr/lib64/pkgconfig/Qt5Sensors.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_sensors.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_sensors_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Sensors.so.5
/usr/lib64/libQt5Sensors.so.5.12
/usr/lib64/libQt5Sensors.so.5.12.0
/usr/lib64/qt5/plugins/sensorgestures/libqtsensorgestures_plugin.so
/usr/lib64/qt5/plugins/sensorgestures/libqtsensorgestures_shakeplugin.so
/usr/lib64/qt5/plugins/sensors/libqtsensors_generic.so
/usr/lib64/qt5/plugins/sensors/libqtsensors_iio-sensor-proxy.so
/usr/lib64/qt5/plugins/sensors/libqtsensors_linuxsys.so
/usr/lib64/qt5/qml/QtSensors/libdeclarative_sensors.so
/usr/lib64/qt5/qml/QtSensors/plugins.qmltypes
/usr/lib64/qt5/qml/QtSensors/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtsensors/LICENSE.FDL
/usr/share/package-licenses/qtsensors/LICENSE.GPL2
/usr/share/package-licenses/qtsensors/LICENSE.GPL3
/usr/share/package-licenses/qtsensors/LICENSE.GPL3-EXCEPT
/usr/share/package-licenses/qtsensors/LICENSE.LGPL3
