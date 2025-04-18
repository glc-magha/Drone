Eğer ROS (Robot Operating System) kullanıyorsan,
MAVROS paketi ile drone uçuşlarını kontrol edebilir ve ROS üzerinden proxy benzeri bir yönlendirme sistemi kurabilirsin.

Temel yapı:

mavros paketi drone'dan veri alır (/mavros/global_position, /mavros/state)

rosbridge veya özel bir node ile bu veriler bir web arayüzüne ya da ikinci ROS sistemine yönlendirilir.

mavros launch dosyası örneği:
<launch>
  <arg name="fcu_url" default="udp://:14540@localhost:14557"/>
  <arg name="gcs_url" default="" />
  <include file="$(find mavros)/launch/px4.launch">
    <arg name="fcu_url" value="$(arg fcu_url)" />
    <arg name="gcs_url" value="$(arg gcs_url)" />
  </include>
</launch>
