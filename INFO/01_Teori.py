"""Drone, genellikle İnsansız Hava Aracı (İHA) olarak bilinir ve hava yoluyla taşıma yapabilen,
yer kontrol istasyonları veya otonom sistemler aracılığıyla yönlendirilen bir araçtır. Droneların temel özellikleri şunlardır:

Otonom uçuş yapabilme: Gelişmiş dronelar, GPS ve sensörler yardımıyla belirli rotalar üzerinde otonom olarak uçabilirler.

Uzaktan kontrol edilebilme: Dronelar, genellikle bir kumanda cihazı veya mobil uygulama ile uzaktan kontrol edilebilirler.

Çeşitli yük taşıma kapasitesi: Drone'lar, kameralar, sensörler, taşıma kargoları gibi farklı yükleri taşıyabilecek şekilde tasarlanabilir.

2. Drone Türleri
Dronelar, kullanım amaçlarına göre farklı kategorilere ayrılabilir. Temel olarak şu türler bulunur:

2.1. Multirotor Dronelar
Multirotor dronelar, en yaygın drone türüdür. Bu tür dronelar, genellikle 4, 6 veya 8 pervane kullanır.
Başlıca çeşitleri şunlardır:

Quadcopter (4 pervane)

Hexacopter (6 pervane)

Octocopter (8 pervane)

Multirotor dronelar, manevra kabiliyetleri ve denge sağlama yetenekleriyle popülerdir.
Genellikle, kameralar ve sensörler gibi yükleri taşımak için kullanılır.

2.2. Tek Rotor Dronelar
Tek rotorlu dronelar, genellikle bir yatay pervane ve bir kuyruk kanat pervanesi ile çalışır.
Bu tür dronelar, daha fazla taşıma kapasitesine sahip olabilirler ve genellikle daha uzun menzilli uçuşlar yapabilirler.
Ancak, manevra kabiliyetleri multirotorlara göre sınırlıdır.

2.3. Kanatlı Dronelar
Kanatlı dronelar, uçaklara benzer yapıya sahip olup, daha uzun mesafelerde uçabilirler.
Bu dronelar, kanatları ile uçmak için hava akımından yararlanır ve sabit kanat yapıları sayesinde
daha düşük enerji tüketimiyle uzun süre havada kalabilirler.
Bu tür dronelar genellikle büyük alanların izlenmesi veya haritalama işleri için kullanılır.

2.4. Hibrid Dronelar
Hibrid dronelar, hem pervaneler hem de kanatlar kullanarak uçabilen araçlardır.
Bu dronelar, hem dikey olarak kalkış ve iniş yapabilme yeteneğine hem de uçak gibi uzun mesafe uçma kapasitesine sahiptir.

3. Drone Bileşenleri
Bir drone, birçok farklı bileşenden oluşur. Bu bileşenler, drone'un uçuş performansını ve işlevselliğini belirler.
Temel bileşenler şunlardır:

3.1. Pervaneler ve Motorlar
Drone('ların uçuşu, pervaneler ve motorlarla sağlanır.'
      ' Pervaneler, hava aracını yukarıya kaldırmak ve manevra yapmasını sağlamak için kullanılır.'
      ' Motorlar ise pervaneleri döndürerek gerekli torku sağlar.'
      ' Pervane sayısı (örneğin, 4 pervaneli bir quadcopter) uçuş özelliklerini doğrudan etkiler.)

3.2. Batarya (Power Supply)
Drone('ların güç kaynağı genellikle lityum-polimer (LiPo) bataryalar ile sağlanır.'
      ' Bu bataryalar, dronelara yüksek enerji yoğunluğu sağlar. '
      'Batarya kapasitesi, drone’un uçuş süresi ve menzilini doğrudan etkiler.)

3.3. Kumanda Sistemi ve Alıcılar
Drone, bir kontrol cihazı aracılığıyla kumanda edilir.
Bu kontrol cihazı, genellikle bir uzaktan kumanda veya mobil cihaz uygulaması olabilir.
Alıcı, kontrol cihazından gelen sinyalleri drone’a ileterek uçuş yönlendirmesini sağlar.

3.4. Sensörler ve GPS
Dronelarda yer alan sensörler, çevresindeki nesneleri algılar ve bu veriler uçuş kontrol sistemine iletilir.
En yaygın sensörler şunlardır:

İvmeölçer (Accelerometer): Drone’un hızını, eğimini ve hareketini ölçer.

Jiroskop: Drone’un dönüş açısını ölçer.

Barometre: Uçuş yüksekliğini ölçer.

GPS: Drone’un konumunu ve rotasını belirler.

Bu sensörler, otonom uçuş, engel tespiti, stabilizasyon gibi işlemleri gerçekleştirir.

3.5. Kamera ve Görüntüleme Sistemleri
Birçok drone, video kaydı yapmak veya fotoğraf çekmek için kameralarla donatılır. Ayrıca, termal kameralar,
multispektral kameralar, LiDAR sistemleri gibi sensörler de drone('larda kullanılabilir. '
Bu tür sistemler, harita yapma, tarım, inşaat, arama-kurtarma gibi alanlarda kullanılır.)

3.6. Uçuş Kontrol Sistemi
Uçuş kontrol sistemi, drone’un tüm uçuşunu yönetir. Uçuş kontrol yazılımı,
sensörlerden gelen verileri işler ve drone’a uçuş komutlarını gönderir.
Uçuş kontrolörü, drone’un stabilitesini sağlamak ve istenilen rotada uçmasını garantilemek için
sürekli olarak pervanelerin hızlarını ayarlar.

4. Drone Teknolojisinin Kullanım Alanları
4.1. Askeri Kullanım
Drone’lar ilk başta askeri alanda keşif, gözetleme ve hedef tespiti için kullanılmıştır.
Bugün, askeri dronelar, istihbarat toplama, saldırılar düzenleme ve lojistik taşımacılık gibi görevlerde kullanılıyor.

4.2. Ticari Kullanım
Ticari alanda dronelar, özellikle tarım, haritalama, inşaat, enerji denetimi gibi sektörlerde yaygın olarak kullanılmaktadır.
Tarımda, dronelar ekin sağlığını izlemek, gübreleme yapmak ve mahsul hasadını optimize etmek için kullanılır.
İnşaat sektöründe ise, projelerin ilerleyişini izlemek ve haritalama yapmak için tercih edilirler.

4.3. Hava Fotoğrafçılığı ve Sinema
Dronelar, hava fotoğrafçılığı ve sinema endüstrisinde popüler bir araçtır.
Dronelar, geleneksel helikopterler ve uçaklardan daha ucuz ve erişilebilir olduğu için
film çekimlerinde ve fotoğrafçılıkta sıklıkla kullanılmaktadır.

4.4. Acil Durum ve Arama-Kurtarma
Dronelar, afet bölgelerinde arama-kurtarma faaliyetlerine yardımcı olmak için kullanılır.
Özellikle erişimi zor bölgelerde, drone’lar arama yapabilir ve hayatta kalanları tespit etmek için termal kameralar kullanabilir.

4.5. Eğlence ve Hobiler
Drone’lar, özellikle eğlence amacıyla kullanıcılara çeşitli uçuş deneyimleri sunar.
Drone yarışları ve havada yapılan akrobasi gösterileri, drone kullanımının popüler bir eğlence alanıdır.

1. Multirotor
Açıklama: Birden fazla pervanesi olan dronelara verilen isimdir. Genellikle 4, 6 veya 8 pervane kullanılır.
Bu tür dronelar, daha stabil uçuş sağlar ve manevra yetenekleri yüksektir. En yaygın türü Quadcopter
(4 pervaneli drone) olup, diğer türler Hexacopter (6 pervane) ve Octocopter (8 pervane) olarak bilinir.

2. Pervane (Propeller)
Açıklama: Drone’un uçuşunu sağlayan döner kanatlardır. Pervaneler, havayı iterek drone('u yukarıya kaldırır.'
'' Pervaneler, uçuşun manevra yeteneğini, stabilitesini ve verimliliğini etkileyen kritik bileşenlerdir.)

3. İvmeölçer (Accelerometer)
Açıklama: Drone’un hızını, yönünü ve hareketini ölçen sensördür.
Bu sensör, drone’un hızlanması veya yavaşlaması hakkında bilgi sağlar.
İvmeölçer, drone’un uçuş stabilitesini korumak için uçuş kontrol sistemiyle sürekli iletişim halindedir.

4. Jiroskop (Gyroscope)
Açıklama: Drone’un dönüş hareketlerini ölçen sensördür. Dönme hızını algılar ve uçuşun stabilitesini sağlamaya yardımcı olur.
Jiroskop, drone’un yatay, dikey ve dönme hareketlerini denetler.

5. Barometre
Açıklama: Uçuş yüksekliğini ölçen sensördür. Genellikle atmosfer basıncını ölçerek, drone’un yerden ne kadar yukarıda olduğunu belirler.
Barometre, özellikle otonom uçuşlarda yüksekliği sabit tutmaya yardımcı olur.

6. GPS (Global Positioning System)
Açıklama: Drone('un konumunu belirlemek için kullanılan bir küresel konumlama sistemidir.'
                ' GPS, drone’a uçuş rotası ve yönü konusunda rehberlik eder. GPS sayesinde drone,
    otonom uçuş yapabilir ve belirli bir hedefe doğru hareket edebilir.)

7. Uçuş Kontrol Sistemi (Flight Controller)
Açıklama: Drone'un uçuşunu yöneten ana donanım bileşenidir. Uçuş kontrolörü, sensörlerden gelen verileri analiz eder ve pervanelerin hızını ayarlayarak stabil uçuş sağlar. Uçuş kontrol sistemi, ayrıca GPS verileri ile yönlendirme yapar ve drone'un dengeyi korumasını sağlar.

8. Gimbal
Açıklama: Kamera ve diğer görüntüleme cihazlarının stabil bir şekilde tutulmasını sağlayan bir cihazdır.
Gimbal, drone uçuşu sırasında kameranın sarsılmadan sabit kalmasını ve düz bir görüntü elde edilmesini sağlar.
Genellikle 2 eksenli (tilt ve pan) veya 3 eksenli (tilt, pan ve roll) olabilir.

9. LiPo Batarya (Lithium Polymer Battery)
Açıklama: Dronelarda en yaygın kullanılan batarya türüdür.
LiPo bataryalar, yüksek enerji yoğunluğu sağlar ve drone’ların uzun süre uçmasını mümkün kılar.
Ancak, LiPo bataryalar dikkatli kullanılması gereken bataryalardır çünkü yüksek sıcaklıklar veya kısa devrelerde patlama riski taşıyabilirler.

10. ESC (Electronic Speed Controller)
Açıklama: Motor hızlarını kontrol etmek için kullanılan elektronik bir cihazdır.
ESC, uçuş kontrolörü tarafından gönderilen komutlara göre motorların hızını ayarlar.
ESC'ler, motorlara enerji akışını düzenler ve drone'un hızını kontrol eder.

11. RTF (Ready to Fly)
Açıklama: Kullanıcıya, drone’u hemen uçurmak için gereken tüm bileşenlerin
(drone, kumanda, batarya, vb.) dahil olduğu drone paketini ifade eder.
Bu, özellikle yeni başlayanlar için kullanımı kolay bir seçenek sunar.

12. FPV (First Person View)
Açıklama: Drone('un kamerasından aldığı canlı video akışını, doğrudan kullanıcıya ileten sistemdir. '
                'FPV, drone kullanıcılarının droneları "ilk şahıs" bakış açısıyla uçurmalarını sağlar. '
                'Bu sistem, drone yarışlarında ve profesyonel çekimlerde yaygın olarak kullanılır.)

13. Otonom Uçuş
Açıklama: Dronenin, insan müdahalesi olmadan belirlenen rotalar üzerinde otomatik olarak uçabilmesidir.
Otonom uçuş, GPS, sensörler ve yazılımlar kullanılarak yapılır.
Otonom uçuş teknolojisi, drone'ları daha verimli ve güvenli hale getirir.

14. Geofence (Coğrafi Sınır)
Açıklama: Drone uçuşları için sanal sınırlar belirleyen bir sistemdir.
Bu sınırlar, drone’un belirli bir alan dışına çıkmasını engeller.
Geofence, genellikle güvenlik amacıyla, drone’ların yasaklı alanlara girmemesi için kullanılır.

15. VLOS (Visual Line of Sight)
Açıklama: Drone('un operatörü tarafından sürekli olarak görsel olarak izlenmesini gerektiren bir uçuş kuralıdır. '
                'VLOS, genellikle yasal düzenlemelerle ilişkilidir ve
            drone pilotunun dronenin uçuşu üzerinde kontrol sahibi olabilmesini sağlar.)

16. Yük Taşıma Kapasitesi
Açıklama: Drone('un taşıyabileceği maksimum ağırlıktır.'
                ' Bu, genellikle drone’un motor gücüne, batarya kapasitesine ve tasarımına bağlıdır.'
                ' Dronelar, çeşitli yükler taşımak için farklı kapasitelere sahip olabilirler (örneğin kamera, sensör, kargo vb.).)

17. Yaw, Pitch, Roll
Açıklama: Bu terimler, drone’un uçuş yönlerini ifade eder:

Yaw: Drone’un yatay eksende döngüsü (sağa/sola dönüş).

Pitch: Drone’un dikey eksende hareketi (yukarı/aşağı).

Roll: Drone’un enine eksende hareketi (sağa/sola eğilme).

18. Hovering
Açıklama: Drone’un belirli bir yükseklikte ve yerde sabit kalması işlemidir.
Hovering, genellikle drone’un stabilizasyonunu sağlamak için kullanılır ve özellikle fotoğraf çekimleri,
video kaydı veya gözlem için gereklidir.

19. Motor Yükü
Açıklama: Motorun taşıdığı yük miktarını ifade eder. Droneların motor yükü, genellikle taşıdığı yük,
batarya kapasitesi ve uçuş hızı ile ilişkilidir.

20. Payload
Açıklama: Drone('un taşıyabileceği ek yükü ifade eder. Bu, genellikle sensörler,'
                ' kameralar, araştırma ekipmanları veya kargo gibi öğeleri içerir.)

21. Gövde Tipi (Frame Type)
Açıklama: Dronenin ana yapısının türüdür. Dronelar genellikle plastik, karbon fiber veya alüminyum gibi hafif,
dayanıklı malzemelerden yapılır. Gövde tipi, drone’un dayanıklılığını ve uçuş verimliliğini etkiler.
1. DRONE'UN TARİHÇESİ (KISA)
İlk İHA çalışmaları askerî amaçlarla 1900'lerin başında başlamıştır.

2000’li yıllarda sivil alana geçiş yaparak fotoğrafçılık, haritalama, lojistik gibi sektörlere yayılmıştır.

2010 sonrası ise ticari drone’lar yaygınlaşarak bireysel kullanıma açılmıştır.

🔧 2. DRONE'UN ANA BİLEŞENLERİ
Drone'lar birçok parçadan oluşur. İşte temel donanımlar:


Bileşen	Görevi
Pervaneler (Propeller)	İtiş gücü sağlar. Genellikle 4 (quad), 6 (hexa) veya 8 (octa) tanedir.
ESC (Electronic Speed Controller)	Motor hızını elektronik olarak kontrol eder.
Fırçasız Motorlar (Brushless Motors)	Pervaneleri döndürür. Sessiz ve verimlidir.
Uçuş Kontrolcü (Flight Controller - FC)	Drone’un “beyni”dir. Sensör verilerini işleyerek stabil uçuş sağlar.
IMU (Inertial Measurement Unit)	Jiroskop ve ivmeölçer ile denge hesaplaması yapar.
GPS Modülü	Konum, yön ve rota takibi için kullanılır.
Batarya (Li-Po genellikle)	Drone’un enerji kaynağıdır. Uçuş süresini belirler.
Kamera / Gimbal	Görüntü alma işlevi. Gimbal titreşimi önleyerek sabit görüntü sağlar.
Radyo Alıcı & Verici (RC Receiver & Transmitter)	Uzaktan kumanda ile drone arasında iletişimi sağlar.
Telemetri Modülü	Uçuş bilgilerini yere iletir. (hız, yükseklik, voltaj vs.)
Frame (Gövde)	Drone’un fiziksel iskeleti. Genellikle karbon fiber ya da plastik.
📡 3. DRONE ÇALIŞMA PRENSİBİ
Drone'lar, pervanelerin dönmesiyle kaldırma kuvveti (lift) oluşturarak havalanır.
 Pervanelerin farklı hızlarda dönmesiyle yön değiştirir, ileri-geri gider, sağa-sola döner (yaw, pitch, roll).

Yukarı/İniş (Throttle): Tüm pervaneler aynı hızda döner.

İleri/Geri (Pitch): Ön veya arka pervaneler daha hızlı döner.

Sağa/Sola Yatış (Roll): Sağ veya sol pervaneler daha hızlı döner.

Dönme (Yaw): Ters yönde dönen pervaneler hız farkı ile döndürür.

📐 4. TEKNİK TERİMLER

Terim	Açıklama
Yaw	Dronun kendi ekseni etrafında dönmesi (sağa-sola dönme)
Pitch	Öne veya arkaya eğilme
Roll	Sola veya sağa yatma
Altitude Hold	Sabit yükseklikte uçma yeteneği
GPS Hold	GPS ile belirli konumu koruma
Return to Home (RTH)	Drone’un kalkış noktasına otomatik geri dönmesi
Failsafe	Sinyal kesilirse önceden belirlenmiş tepki (örneğin iniş)
Loiter Mode	Belirli noktada sabit kalma (genellikle GPS ile)
Waypoint	Önceden belirlenmiş noktalara otonom uçuş
FPV (First Person View)	Kameradan canlı görüntü ile uçuş
Telemetry	Uçuş verilerinin gerçek zamanlı iletilmesi (hız, batarya, irtifa vb.)
🧠 5. DRONE KONTROL YÖNTEMLERİ
Manuel Kontrol: Kullanıcı her hareketi kendisi yönetir.

Yarı-Otonom (Assisted): Yükseklik koruma, yön sabitleme gibi yardımlar sağlar.

Tam Otonom: GPS + yazılım ile harita üstünde otomatik rota izler.

📷 6. DRONE TÜRÜNE GÖRE KULLANIM ALANLARI

Tür / Sınıf	Kullanım Alanı
Hobi (RC Drone)	Eğlence, FPV yarışları
Kamera Dronları	Fotoğrafçılık, sinema çekimi
Endüstriyel Drone	Tarım (ilaçlama, haritalama), enerji (hat denetimi)
Lojistik Drone	Kargo, teslimat hizmetleri
Askerî İHA’lar	Keşif, gözetleme, saldırı amaçlı
Yarış Dronları	FPV yarışları, hız ve çeviklik üzerine tasarlanır.
Multi-Rotor	Yaygın olan tip (Quadcopter, Hexacopter)
Fixed-Wing	Sabit kanatlı, uzun menzilli uçuşlar için
VTOL (Vertical Takeoff and Landing)	Helikopter gibi dikey kalkar, uçak gibi uçar.
⚙️ 7. YAZILIM & UÇUŞ KONTROL SİSTEMLERİ
Drone’lar genellikle açık kaynaklı veya özel yazılımlar kullanır:

Ardupilot – Gelişmiş otomatik uçuş özellikleri sağlar.

PX4 – Drone yazılım mimarisi (Linux tabanlı).

Betaflight / Cleanflight – FPV yarış dronları için optimize.

DJI Flight Software – DJI marka cihazlar için özel kontrol yazılımı.

Mission Planner / QGroundControl – Harita üzerinden rota planlama.

🔋 8. BATARYA ve GÜÇ YÖNETİMİ
En yaygın batarya tipi: Li-Po (Lityum Polimer).

mAh (miliamper-saat): Kapasiteyi gösterir.

C-Rate: Boşaltma oranı (yüksek C → hızlı boşalır).

Uçuş süresi: Genelde 15–30 dakika arasıdır.

Aşırı şarj veya tam boşaltma bataryaya zarar verir!

🛠️ 9. DRONE MONTAJ VE KALİBRASYON SÜRECİ
Frame montajı

Motor ve ESC bağlantısı

Flight Controller yerleştirme

GPS ve sensörlerin takılması

RC sistem bağlantısı

Kalibrasyon (IMU, compass, ESC)

Test uçuşu ve PID ayarları

⚖️ 10. DRONE UÇUŞ KURALLARI (Türkiye İçin)
Sivil Havacılık Genel Müdürlüğü (SHGM) kayıt zorunluluğu vardır (500g üstü).

Şehir içinde, kalabalık alanlarda uçmak yasaktır.

120 metre üzeri irtifalar izne tabidir.

Askerî tesis, havaalanı yakınlarında uçmak yasaktır.

Uçuş öncesi İHA Kayıt Sistemi’ne (iharegister.shgm.gov.tr) kayıt gereklidir.

"""