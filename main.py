import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. SAYFA YAPILANDIRMASI VE GÖZÜ YORMAYAN MODERN TASARIM (CSS & JS)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Zaman Metafiziği & Bilimsel Perspektif",
    page_icon="⏳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Gözü yormayan, yumuşak renk paleti (Yumuşak Krem/Gri Arka Plan, Koyu Gri Yazılar, Sakin Tonlar)
eye_friendly_css_js = """
<style>
    /* Genel Arka Plan ve Yazı Renkleri */
    .stApp {
        background-color: #F4F6F9;
        color: #2C3E50;
    }
    
    /* Metin Seçimi ve Kopyalama Engelleme */
    * {
        -webkit-user-select: none !important;
        -moz-user-select: none !important;
        -ms-user-select: none !important;
        user-select: none !important;
    }
    @media print {
        body { display: none !important; }
    }

    /* Kart Tasarımları (Gözü yormayan yumuşak beyaz/gri kartlar) */
    .info-card {
        background-color: #FFFFFF;
        border-left: 5px solid #2980B9;
        padding: 22px;
        border-radius: 10px;
        margin-bottom: 18px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
        transition: transform 0.2s ease;
    }
    .info-card:hover {
        transform: translateY(-2px);
    }
    .card-title {
        color: #1B4F72;
        font-weight: 700;
        font-size: 1.15rem;
        margin-bottom: 8px;
    }
    .card-text {
        color: #34495E;
        font-size: 1.02rem;
        line-height: 1.7;
    }
    .card-source {
        color: #7F8C8D;
        font-size: 0.85rem;
        font-style: italic;
        margin-top: 12px;
        text-align: right;
    }

    /* Hukuki Uyarı ve Alt Bantlar */
    .legal-banner {
        background-color: #EBF5FB;
        border: 1px solid #AED6F1;
        color: #1B4F72;
        padding: 15px;
        border-radius: 8px;
        font-size: 0.9rem;
        text-align: center;
        margin-top: 35px;
    }
    
    /* Sidebar (Kenar Çubuğu) Yumuşatma */
    [data-testid="stSidebar"] {
        background-color: #EAECEE;
    }
</style>

<script>
    const doc = window.parent.document;
    doc.addEventListener('contextmenu', event => event.preventDefault());
    doc.addEventListener('copy', event => { event.preventDefault(); return false; });
    doc.addEventListener('cut', event => { event.preventDefault(); return false; });
    doc.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && 
            (e.key === 'c' || e.key === 'C' || 
             e.key === 'u' || e.key === 'U' || 
             e.key === 's' || e.key === 'S' || 
             e.key === 'p' || e.key === 'P' || 
             e.key === 'a' || e.key === 'A')) {
            e.preventDefault();
            return false;
        }
        if (e.key === 'F12') {
            e.preventDefault();
            return false;
        }
    });
</script>
"""
st.markdown(eye_friendly_css_js, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. ÇİFT DİLLİ VERİTABANI (TÜRKÇE / İNGİLİZCE)
# -----------------------------------------------------------------------------
DATA = {
    "TR": {
        "app_title": "⏳ ZAMANIN HİKMETİ, BEREKETİ VE BİLİMSEL PERSPEKTİFİ",
        "app_subtitle": "İslam Düşüncesi, Tasavvuf, Risale-i Nur ve Modern Fizik Işığında Zaman Analizi",
        "nav_title": "Bölümler",
        "sections": [
            "1. Zaman Nedir? & Zamanın Önemi",
            "2. Zaman Genişlemesi ve Daralması",
            "3. Kur'an-ı Kerim'de Zaman (Diyanet Meali)",
            "4. Hadis-i Şeriflerde Zaman (15 Hadis)",
            "5. Bediüzzaman Said Nursi'nin Görüşleri (15 Madde)",
            "6. Evliya ve Veli Kulların Görüşleri (15 Büyük Veli)",
            "7. Bilim İnsanlarının Görüşleri ve Fizik Teorileri (15 Bilim İnsanı)",
            "8. Hukuki Uyarı ve Telif Hakları"
        ],
        "legal_short": "⚠️ HUKUKİ UYARI: Bu yazılım yalnızca bilgi ve tefekkür amaçlıdır. İçeriklerin kopyalanması, çoğaltılması ve ticari amaçla kullanılması yasaktır.",
        "sec1_title": "Zaman Nedir ve Neden En Büyük Sermayedir?",
        "sec1_content": [
            {
                "title": "Zamanın Mahiyeti",
                "text": "Zaman; kâinattaki hareket, değişim ve oluşların ölçüsü olan soyut bir boyuttur. İslam kelamcılarına göre zaman, Cenab-ı Hakk'ın 'Ed-Dehr' isminin bir tecellisidir, hadiselerin birbirini takip etme düzenidir.",
                "source": "İslam Felsefesi ve Kelam Literatürü"
            },
            {
                "title": "Zamanın Önemi ve İnsan Ömrü",
                "text": "İnsan ömrü, kendisine emanet edilmiş en kıymetli ve telafisi imkansız sermayedir. Geçen her saniye, ebedi hayatın tarlasına ekilen bir tohumdur.",
                "source": "İmam Gazali - İhyâu Ulûmi'd-Dîn"
            }
        ],
        "sec2_title": "Zaman Genişlemesi ve Daralması",
        "sec2_content": [
            {
                "title": "Bast-ı Zaman (Zamanın Genişlemesi)",
                "text": "Tasavvufta kısa bir zaman dilimine çok uzun işlerin sığdırılmasıdır. Modern fizikteki İzafiyet Teorisi ile kavramsal bir paralellik gösterir.",
                "source": "Tasavvuf Istılahları & Modern Fizik"
            },
            {
                "title": "Zamanın Daralması (Ahirzaman Bereket Kaybı)",
                "text": "Zamanın bereketinin azalmasıyla günlerin hızla akıp gitmesi ve yapılan işlerden manevi verim alınamaması halidir.",
                "source": "Hadis ve Tasavvuf Kaynakları"
            }
        ],
        "verses": [
            {"surah": "Asr Suresi, 1-3. Ayetler", "text": "Andolsun zamana ki, insan gerçekten ziyan içindedir. Ancak, iman edip de sâlih ameller işleyenler, birbirlerine hakkı ve sabrı tavsiye edenler başka.", "source": "Kur'an-ı Kerim (Diyanet Meali)"},
            {"surah": "Hac Suresi, 47. Ayet", "text": "...Şüphesiz Rabbinin katında bir gün, sizin saymakta olduklarınızdan bin yıl gibidir.", "source": "Kur'an-ı Kerim (Diyanet Meali)"},
            {"surah": "Mearic Suresi, 4. Ayet", "text": "Melekler ve Ruh O'na, süresi elli bin yıl olan bir günde yükselirler.", "source": "Kur'an-ı Kerim (Diyanet Meali)"},
            {"surah": "Secde Suresi, 5. Ayet", "text": "...Sonra bu işler, süresi sizin hesabınızla bin yıl olan bir günde O'na yükselir.", "source": "Kur'an-ı Kerim (Diyanet Meali)"},
            {"surah": "Yunus Suresi, 45. Ayet", "text": "Onları toplayacağı gün, sanki dünyada gündüzün ancak bir saati kadar kaldıklarını sanırlar...", "source": "Kur'an-ı Kerim (Diyanet Meali)"},
            {"surah": "Mü'minun Suresi, 112-113. Ayetler", "text": "Allah 'Yeryüzünde kaç yıl kaldınız?' der. Onlar 'Bir gün veya günün bir kısmı kadar kaldık' derler.", "source": "Kur'an-ı Kerim (Diyanet Meali)"},
            {"surah": "Furkan Suresi, 62. Ayet", "text": "O, öğüt almak isteyen kimseler için geceyi ve gündüzü birbiri ardınca getirendir.", "source": "Kur'an-ı Kerim (Diyanet Meali)"},
            {"surah": "İbrahim Suresi, 33. Ayet", "text": "O, güneşi ve ayı, geceyi ve gündüzü sizin emrinize verendir.", "source": "Kur'an-ı Kerim (Diyanet Meali)"},
            {"surah": "Münafikun Suresi, 10. Ayet", "text": "Ölüm gelip de 'Rabbim beni yakın bir zamana kadar geciktirsen!' demeden önce infak edin.", "source": "Kur'an-ı Kerim (Diyanet Meali)"},
            {"surah": "İsra Suresi, 12. Ayet", "text": "Biz geceyi ve gündüzü iki delil kıldık... yılların sayısını ve hesabını bilesiniz diye.", "source": "Kur'an-ı Kerim (Diyanet Meali)"}
        ],
        "hadiths": [
            {"title": "1. İki Büyük Nimet", "text": "İki nimet vardır ki insanların çoğu aldanmıştır: Sağlık ve boş vakit.", "source": "Buhârî, Rikâk, 1"},
            {"title": "2. Beş Şey Gelmeden Önce", "text": "Gençliğini ihtiyarlığından, sağlığını hastalığından, zenginliğini fakirliğinden önce bil.", "source": "Hâkim, Müstedrek, IV, 341"},
            {"title": "3. Zamana Sövme Yasağı", "text": "Âdemoğlu zamana söverek beni üzer; çünkü zaman benim, geceyi ve gündüzü ben çeviririm.", "source": "Buhârî, Tefsîr, 45/1"},
            {"title": "4. Sorgu Soruları", "text": "Kıyamet günü kul ömrünü ve gençliğini nerede tükettiğinden sorguya çekilmedikçe ayrılamaz.", "source": "Tirmizî, Sıfatü'l-Kıyâme, 1"},
            {"title": "5. Zamanın Daralması", "text": "Zaman yaklaşmadıkça kıyamet kopmaz; bir yıl ay gibi, bir ay hafta gibi geçer.", "source": "Tirmizî, Zühd, 24"},
            {"title": "6. Malangâniyi Terk", "text": "Kişinin malayani (boş) şeyleri terk etmesi İslam'ının güzelliğindendir.", "source": "Tirmizî, Zühd, 11"},
            {"title": "7. Yolcu Gibi Yaşamak", "text": "Dünyada bir garip veya yolcu gibi ol.", "source": "Buhârî, Rikâk, 3"},
            {"title": "8. Fidan Dikmek", "text": "Kıyamet koparken elinizde fidan varsa ve dikmeye gücünüz yetiyorsa dikin.", "source": "Ahmed b. Hanbel, III, 191"},
            {"title": "9. Sabahın Bereketi", "text": "Allah'ım, ümmetimin sabah erkenden yapılan işlerini bereketli kıl.", "source": "Ebû Dâvûd, Cihâd, 78"},
            {"title": "10. Erteleyenlerin Helaki", "text": "Yarın yaparım diyerek erteleyenler helak olmuştur.", "source": "Aclûnî, Keşfü'l-Hafâ"},
            {"title": "11. Vakit Kılıç Gibidir", "text": "Vakit keskin bir kılıç gibidir; sen onu kesmezsen o seni keser.", "source": "İmam Şâfiî / Tasavvuf Literatürü"},
            {"title": "12. İki Günü Eşit Olan", "text": "İki günü birbirine eşit olan ziyandadır.", "source": "Deylemî, Müsnedü'l-Firdevs"},
            {"title": "13. Hayırlı Ömür", "text": "İnsanların en hayırlısı ömrü uzun ve ameli güzel olandır.", "source": "Tirmizî, Zühd, 21"},
            {"title": "14. Eskiten Zaman", "text": "Gece ve gündüz yeni olan her şeyi eskitir.", "source": "Taberânî, el-Mu'cemü'l-Evsat"},
            {"title": "15. Ölümü Hatırlamak", "text": "Lezzetleri acılaştıran ölümü çokça hatırlayın.", "source": "Tirmizî, Zühd, 4"}
        ],
        "bediuzzaman": [
            {"title": "1. Mazi ve Müstakbelin Hakikati", "text": "Geçmiş ve gelecek hayali ve yok anlardır; insan sadece içinde bulunduğu hâl anından sorumludur.", "source": "Sözler, 21. Söz"},
            {"title": "2. Kadir Gecesi ve Zamanın Genişlemesi", "text": "Seksen yıllık bir ömrü bir geceye sığdıran Bast-ı Zaman hakikatidir.", "source": "Şualar"},
            {"title": "3. Miraç ve Zaman Ötesi Seyahat", "text": "Peygamberimizin yatağı soğumadan binlerce yıllık mesafeyi aşması ruhun zamanı aşmasıdır.", "source": "Sözler, 31. Söz"},
            {"title": "4. Dönen Ateş Noktası", "text": "Hızla döndürülen ateş kıvılcımının çember görünmesi gibi, kainat da ilahi kudretin süratiyle bir anlık yaratılış nehridir.", "source": "Mektubat"},
            {"title": "5. Sinema Şeridi Teşbihi", "text": "Zaman karelerden oluşan şerittir; biz içinde yaşarken Yaratıcı bütün şeridi birden görür.", "source": "Mesnevi-i Nuriye"},
            {"title": "6. Çekirdek ve Ağaç", "text": "Tarihçesi çekirdeğe dercedilen ağaç gibi zaman da kaderin maddeye açılmasıdır.", "source": "Sözler, 26. Söz"},
            {"title": "7. Beş Vakit Namaz", "text": "Namaz, günün dağılan zamanını toplayan ilahi bir disiplindir.", "source": "Sözler, 9. Söz"},
            {"title": "8. İman Gözlüğüyle Zaman", "text": "İman, geçmişi dostlar meclisine, geleceği rahmet sarayına çevirir.", "source": "Asa-yı Musa"},
            {"title": "9. Fani Ömrü Baki Kılmak", "text": "Allah rızası için yapılan amel fani dakikayı ebedileştirir.", "source": "Lem'alar"},
            {"title": "10. Askerlik Nöbeti ve Sabır", "text": "İnsan sadece bugünkü nöbetinden ve anından sorumludur.", "source": "Sözler, 21. Söz"},
            {"title": "11. Kainat Saati", "text": "Kainat saniye, dakika ve asırları sayan muazzam bir saattir.", "source": "Sözler, 29. Söz"},
            {"title": "12. İhlasın Bereketi", "text": "İhlasla geçirilen bir dakika bin seneden üstündür.", "source": "Lem'alar"},
            {"title": "13. Rüya Alemi", "text": "Rüyada saniyelerin yıllar gibi yaşanması zamanın izafiliğini gösterir.", "source": "Mektubat"},
            {"title": "14. Misafirhane", "text": "Dünya misafirhanesinde yolcu olan insan ebedi vatanına hazırlanır.", "source": "Sözler, 23. Söz"},
            {"title": "15. Lezzetlerin Zevali", "text": "Haram lezzet bir dakikada biter, vebali kalır; ibadet meşakkati biter, nuru baki kalır.", "source": "Sözler, 13. Söz"}
        ],
        "saints": [
            {"name": "1. İmam-ı Rabbani", "quote": "İbnü'l-vakt olan derviş ne geçmişle ne gelecekle meşgul olur; o an Allah'ın rızasına odaklanır.", "source": "Mektubat-ı Rabbani"},
            {"name": "2. Abdülkadir Geylani", "quote": "Her nefes geri gelmeyen bir cevherdir, zayi edilmemelidir.", "source": "Fütûhu'l-Gayb"},
            {"name": "3. Mevlana Celaleddin-i Rumi", "quote": "Dün geçti, yarın gelmedi; sen bugünü ganimet bil.", "source": "Mesnevi"},
            {"name": "4. İmam Gazali", "quote": "Ömür sayılı nefeslerdir, ilim ve ibadetle kıymet kazanır.", "source": "İhyâu Ulûmi'd-Dîn"},
            {"name": "5. Şah-ı Nakşibend", "quote": "Vukuf-u zamani ile her an kalbin halini denetlemek esastır.", "source": "Reşahat"},
            {"name": "6. Muhyiddin İbnü'l-Arabi", "quote": "Kalp safiyete erince zaman dürülür ve alemler seyredilir.", "source": "Fütûhât-ı Mekkiyye"},
            {"name": "7. Hasan-ı Basri", "quote": "Sen günlerden ibaretsin, bir günün geçmesi parçanın gitmesidir.", "source": "Hilyetü'l-Evliya"},
            {"name": "8. Cüneyd-i Bağdadi", "quote": "Vakit iki nefes arasındaki çizgidir.", "source": "Risale-i Kuşeyriyye"},
            {"name": "9. Yunus Emre", "quote": "Aşık için zaman eskimez, her dem yeniden tazelenir.", "source": "Divan"},
            {"name": "10. Aziz Mahmud Hüdayi", "quote": "Zaman hızla akan bir seldir, zikir ve amel ile gemi kurulmalıdır.", "source": "Tarikatname"},
            {"name": "11. İbrahim Hakkı Erzurumi", "quote": "Her saniye ebediyet sarayına konulan bir kerpiçtir.", "source": "Marifetname"},
            {"name": "12. Beyazıd-ı Bistami", "quote": "Hakikat ehli vaktine hükmeder.", "source": "Tezkiretü'l-Evliya"},
            {"name": "13. Ebu'l-Hasan Harakani", "quote": "Nefesler arasında gafletten uyanık olmak gerekir.", "source": "Nefahatü'l-Üns"},
            {"name": "14. Somuncu Baba", "quote": "Ömür buz gibi erimeden kullukla iksirleşmelidir.", "source": "Menakıbname"},
            {"name": "15. Hacı Bayram-i Veli", "quote": "Gönül yapmaya adanan ömür ebedileşir.", "source": "Divan-ı İlahiyat"}
        ],
        "scientists": [
            {"name": "1. Sir Isaac Newton", "theory": "Mutlak Zaman ve Uzay", "text": "Newton'a göre zaman; evrenden bağımsız, her yerde ve her an aynı hızla ve değişmez şekilde akan mutlak bir fonksiyondur.", "source": "Philosophiae Naturalis Principia Mathematica (1687)"},
            {"name": "2. Albert Einstein", "theory": "Özel ve Genel Görelilik", "text": "Zaman mutlak değildir; gözlemcinin hızına ve yerçekimi alanına göre göreceli olarak esner, yavaşlar veya hızlanır (Zaman Genişlemesi).", "source": "Zur Elektrodynamik bewegter Körper (1905)"},
            {"name": "3. Hermann Minkowski", "theory": "Dört Boyutlu Uzay-Zaman Geometrisi", "text": "Einstein'ın teorisini geometrikleştirerek zamanı dördüncü boyut olarak tanımlamıştır.", "source": "Space and Time Konferansı (1908)"},
            {"name": "4. Ludwig Boltzmann", "theory": "Termodinamik Zaman ve Entropi (Zamanın Ok'u)", "text": "Zamanın tek yönlü akışını evrendeki düzensizliğin (entropi) sürekli artmasıyla açıklamıştır.", "source": "Lectures on Gas Theory (1896)"},
            {"name": "5. Stephen Hawking", "theory": "Kozmolojik Zaman ve Başlangıç", "text": "Büyük Patlama ile zamanın da bir başlangıcı olduğunu, evrenin sınırları olmadığını savunmuştur.", "source": "A Brief History of Time (1988)"},
            {"name": "6. Ilya Prigogine", "theory": "Zamanın Dönüşümsüzlüğü ve Kaos", "text": "Karmaşık termodinamik sistemlerde zamanın geri alınamaz (dönüşümsüz) bir evrim gösterdiğini kanıtlamıştır.", "source": "The End of Certainty (1996)"},
            {"name": "7. Carlo Rovelli", "theory": "Döngüsel Kuantum Kravitesi ve Zamanın Yanılsaması", "text": "Temel kuantum seviyesinde zamanın fundamental bir fiziksel büyüklük olmadığını öne sürmüştür.", "source": "The Order of Time (2017)"},
            {"name": "8. Julian Barbour", "theory": "Zamanın Sonu ve Değişmezlik", "text": "Evrenin zaman akışına sahip olmadığını, her anın ayrı ve bağımsız bir 'şimdi' tablosu olduğunu savunmuştur.", "source": "The End of Time (1999)"},
            {"name": "9. Max Planck", "theory": "Planck Zamanı", "text": "Fiziksel olarak ölçülebilecek en kısa zaman birimini bularak zamanın kesikli yapısını ortaya koymuştur.", "source": "Quantum Theory Derlemeleri (1899)"},
            {"name": "10. John Wheeler", "theory": "Geometrodinamik ve Kuantum Köpüğü", "text": "Planck ölçeğinde uzay-zaman dokusunun pürüzsüz olmadığını, çalkantılı bir yapı sergilediğini öne sürmüştür.", "source": "Geometrodynamics (1962)"},
            {"name": "11. Arthur Eddington", "theory": "Zamanın Ok'u (Arrow of Time)", "text": "Fiziksel olarak tersine çevrilemeyen süreçlerin evrenin entropi artışıyla yön kazandığını ifade etmiştir.", "source": "The Nature of the Physical World (1928)"},
            {"name": "12. Erwin Schrödinger", "theory": "Kuantum Dalga Denklemi ve Zaman Evrimi", "text": "Kuantum sistemlerinin durumlarının zaman içinde nasıl değiştiğini modellemiştir.", "source": "Annalen der Physik (1926)"},
            {"name": "13. Hendrik Lorentz", "theory": "Lorentz Dönüşümleri", "text": "Einstein öncesinde hareketli cisimlerde zamanın yavaşlamasını formüle eden fizikçidir.", "source": "Electromagnetic Phenomena (1904)"},
            {"name": "14. Henri Poincaré", "theory": "Eşzamanlılığın Göreliliği", "text": "Zaman ölçümünün mutlak olmadığını, ışık sinyallerinin iletim hızına bağlı olduğunu savunmuştur.", "source": "Science and Hypothesis (1902)"},
            {"name": "15. Kurt Gödel", "theory": "Gödel Evreni ve Zaman Yolculuğu", "text": "Genel görelilik denklemlerine dayanarak dönen bir evrende zaman döngüleri olabileceğini göstermiştir.", "source": "An Example of a New Type of Cosmological Solutions (1949)"}
        ],
        "legal_full": """
        ### ⚖️ HUKUKİ KORUMA VE TELİF HAKLARI BİLDİRİMİ
        
        1. *Bilgi ve Tefekkür Amaçlıdır:* Bu yazılım platformunda yer alan tüm metinler, derlemeler ve tasnifler yalnızca bireysel eğitim ve araştırma amacıyla sunulmuştur.
        2. *Ticari Kullanım Yasağı:* Bu yazılımın ticari amaçla satılması, kiralanması kesinlikle yasaktır.
        3. *Kopyalama ve Çoğaltma Koruması:* 5846 Sayılı Fikir ve Sanat Eserleri Kanunu uyarınca korunmaktadır.
        """
    },
    "EN": {
        "app_title": "⏳ WISDOM, BLESSING AND SCIENTIFIC PERSPECTIVE OF TIME",
        "app_subtitle": "Analysis of Time through Islamic Thought, Sufism, Risale-i Nur, and Modern Physics",
        "nav_title": "Sections",
        "sections": [
            "1. What is Time? & Importance",
            "2. Time Dilation & Contraction",
            "3. Time in the Holy Quran (Diyanet)",
            "4. Time in Hadith Sharif (15 Hadiths)",
            "5. Bediuzzaman Said Nursi's Views (15 Items)",
            "6. Views of Saints / Awliya (15 Saints)",
            "7. Views of Scientists & Physics Theories (15 Scientists)",
            "8. Legal Notice & Copyright Protection"
        ],
        "legal_short": "⚠️ LEGAL NOTICE: This software is for informational and contemplative purposes only. Copying and commercial use are strictly prohibited.",
        "sec1_title": "What is Time and Why is it Greatest Capital?",
        "sec1_content": [
            {
                "title": "The Nature of Time",
                "text": "Time is an abstract dimension measuring motion and change. In Islamic theology, it is a manifestation of Allah's Name 'Ad-Dahr'.",
                "source": "Islamic Philosophy & Kalam"
            },
            {
                "title": "Importance of Time",
                "text": "Human lifespan is the most precious capital. Every passing second is a seed for eternity.",
                "source": "Imam Al-Ghazali - Ihya"
            }
        ],
        "sec2_title": "Time Dilation and Contraction",
        "sec2_content": [
            {
                "title": "Bast-ı Zaman (Time Dilation)",
                "text": "Fitting long accomplishments into a brief moment in Sufism, paralleled conceptually by relativistic time dilation.",
                "source": "Sufism & Modern Physics"
            },
            {
                "title": "Contraction of Time",
                "text": "The rapid passing of days and loss of spiritual blessing in the end times.",
                "source": "Hadith & Sufi Sources"
            }
        ],
        "verses": [
            {"surah": "Surah Al-Asr, 1-3", "text": "By time, indeed, mankind is in loss, except those who believe and do righteous deeds...", "source": "Holy Quran (Diyanet Translation)"},
            {"surah": "Surah Al-Hajj, 47", "text": "...Indeed, a day with your Lord is like a thousand years of those which you count.", "source": "Holy Quran (Diyanet Translation)"},
            {"surah": "Surah Al-Ma'arij, 4", "text": "The angels and the Spirit ascend to Him during a Day the extent of which is fifty thousand years.", "source": "Holy Quran (Diyanet Translation)"},
            {"surah": "Surah As-Sajdah, 5", "text": "...Then it will ascend to Him in a Day, the extent of which is a thousand years.", "source": "Holy Quran (Diyanet Translation)"},
            {"surah": "Surah Yunus, 45", "text": "And on the Day when He will gather them, as if they had not remained but an hour...", "source": "Holy Quran (Diyanet Translation)"},
            {"surah": "Surah Al-Mu'minun, 112-113", "text": "He will say 'How many years did you remain?' They will say 'A day or part of a day.'", "source": "Holy Quran (Diyanet Translation)"},
            {"surah": "Surah Al-Furqan, 62", "text": "And it is He who made the night and day in succession...", "source": "Holy Quran (Diyanet Translation)"},
            {"surah": "Surah Ibrahim, 33", "text": "And He subjected for you the sun, moon, night and day.", "source": "Holy Quran (Diyanet Translation)"},
            {"surah": "Surah Al-Munafiqun, 10", "text": "And spend before death approaches and one says 'My Lord, delay me for a brief term!'", "source": "Holy Quran (Diyanet Translation)"},
            {"surah": "Surah Al-Isra, 12", "text": "And We made the night and day two signs to know the number of years and count.", "source": "Holy Quran (Diyanet Translation)"}
        ],
        "hadiths": [
            {"title": "1. Two Blessings", "text": "Two blessings which many people lose: health and free time.", "source": "Sahih al-Bukhari, Riqaq, 1"},
            {"title": "2. Five Before Five", "text": "Take advantage of youth before old age, health before sickness...", "source": "Al-Hakim, Mustadrak"},
            {"title": "3. Prohibition of Cursing Time", "text": "Do not curse time, for Allah is Time.", "source": "Sahih al-Bukhari, Tafsir"},
            {"title": "4. Judgment Day Questions", "text": "Feet will not move until asked about life and youth.", "source": "Tirmidhi, 2417"},
            {"title": "5. Contraction of Time", "text": "Time will constrict; a year like a month...", "source": "Tirmidhi, Zuhd, 24"},
            {"title": "6. Leaving Vain Things", "text": "Leaving what does not concern you is part of Islam's perfection.", "source": "Tirmidhi, Zuhd, 11"},
            {"title": "7. Traveler Analogy", "text": "Be in this world as a stranger or traveler.", "source": "Sahih al-Bukhari, Riqaq, 3"},
            {"title": "8. Planting a Sapling", "text": "Plant it even if the Hour is establishing.", "source": "Musnad Ahmad"},
            {"title": "9. Morning Blessings", "text": "O Allah, bless my nation in their early mornings.", "source": "Abu Dawud, Jihad, 78"},
            {"title": "10. Procrastinators", "text": "Those who procrastinate are ruined.", "source": "Ajluni, Kashf al-Khafa"},
            {"title": "11. Time as Sword", "text": "Time is like a sharp sword.", "source": "Imam Al-Shafi'i"},
            {"title": "12. Equal Days", "text": "He whose two days are equal is at a loss.", "source": "Daylami"},
            {"title": "13. Best of People", "text": "Long life and good deeds.", "source": "Tirmidhi, Zuhd, 21"},
            {"title": "14. Wearing Out", "text": "Night and day wear out everything new.", "source": "Tabarani"},
            {"title": "15. Destroyer of Pleasures", "text": "Remember death frequently.", "source": "Tirmidhi, Zuhd, 4"}
        ],
        "bediuzzaman": [
            {"title": "1. Past and Future", "text": "Past and future are nonexistent; man is responsible for the present moment.", "source": "The Words, 21st Word"},
            {"title": "2. Night of Power", "text": "Eighty years compressed into a single night (Bast-ı Zaman).", "source": "The Rays"},
            {"title": "3. Ascension (Miraj)", "text": "Transcending millennia while the bed is still warm.", "source": "The Words, 31st Word"},
            {"title": "4. Spinning Ember", "text": "Continuous creation perceived as a river due to Divine speed.", "source": "The Letters"},
            {"title": "5. Cinema Film Strip", "text": "Time as frames; Creator observes the whole strip simultaneously.", "source": "Mesnevi-i Nuriye"},
            {"title": "6. Seed and Tree", "text": "Destiny unfolding into matter over time.", "source": "The Words, 26th Word"},
            {"title": "7. Daily Prayers", "text": "Divine discipline resetting the soul's clock.", "source": "The Words, 9th Word"},
            {"title": "8. Lens of Faith", "text": "Faith turns past into friendly assembly and future into paradise.", "source": "Asa-yı Musa"},
            {"title": "9. Eternalizing Life", "text": "Sincere deeds turn transient moments into eternal fruits.", "source": "The Flashes"},
            {"title": "10. Military Watch", "text": "Focusing patience solely on today's watch.", "source": "The Words, 21st Word"},
            {"title": "11. Cosmic Clock", "text": "Universe as a magnificent clock counting seconds and centuries.", "source": "The Words, 29th Word"},
            {"title": "12. Sincerity", "text": "One minute with sincerity outweighs a thousand years.", "source": "The Flashes"},
            {"title": "13. Dream Realm", "text": "Experiencing years in seconds during dreams.", "source": "The Letters"},
            {"title": "14. Guesthouse", "text": "Man as a traveler preparing for the eternal home.", "source": "The Words, 23rd Word"},
            {"title": "15. Vanishing Pleasures", "text": "Illicit pleasures end in a minute; spiritual rewards remain forever.", "source": "The Words, 13th Word"}
        ],
        "saints": [
            {"name": "1. Imam Rabbani", "quote": "The dervish of the present moment focuses on Allah's pleasure right now.", "source": "Maktubat-i Rabbani"},
            {"name": "2. Abdul Qadir Gilani", "quote": "Every breath is an irreplaceable jewel.", "source": "Futuh al-Ghayb"},
            {"name": "3. Mawlana Rumi", "quote": "Yesterday has passed, tomorrow is unreached; seize today.", "source": "Masnavi"},
            {"name": "4. Imam Al-Ghazali", "quote": "Life is numbered breaths.", "source": "Ihya Ulum al-Din"},
            {"name": "5. Bahauddin Naqshband", "quote": "Awareness of time (Wuquf-i Zamani) audits the heart.", "source": "Rashahat"},
            {"name": "6. Ibn Arabi", "quote": "When the heart is purified, time is folded.", "source": "Al-Futuhat al-Makkiyya"},
            {"name": "7. Hasan al-Basri", "quote": "You are a collection of days.", "source": "Hilyat al-Awliya"},
            {"name": "8. Junayd al-Baghdadi", "quote": "Time is the fine line between breaths.", "source": "Al-Risala"},
            {"name": "9. Yunus Emre", "quote": "Time never grows old for the lover of Truth.", "source": "Divan"},
            {"name": "10. Aziz Mahmud Hudayi", "quote": "Turn the flood of time into a sturdy ship.", "source": "Tarikatname"},
            {"name": "11. Ibrahim Hakki", "quote": "Every second is a brick in the palace of eternity.", "source": "Marifetname"},
            {"name": "12. Bayazid Bastami", "quote": "The gnostic rules over time.", "source": "Tadhkirat"},
            {"name": "13. Abu'l-Hasan Kharaqani", "quote": "Keep the heart awake between breaths.", "source": "Nafahat"},
            {"name": "14. Somuncu Baba", "quote": "Life melts like ice unless transformed by servitude.", "source": "Chronicles"},
            {"name": "15. Haci Bayram-i Veli", "quote": "Time dedicated to mending hearts becomes eternal.", "source": "Divan-i Ilahiyat"}
        ],
        "scientists": [
            {"name": "1. Sir Isaac Newton", "theory": "Absolute Time and Space", "text": "Time flows independently of everything external, universally uniform and absolute.", "source": "Principia Mathematica (1687)"},
            {"name": "2. Albert Einstein", "theory": "Special & General Relativity", "text": "Time is relative, dependent on speed and gravity (Time Dilation), forming Spacetime.", "source": "Electrodynamics of Moving Bodies (1905)"},
            {"name": "3. Hermann Minkowski", "theory": "Four-Dimensional Spacetime", "text": "Space and time merge into a unified four-dimensional geometry.", "source": "Space and Time Lecture (1908)"},
            {"name": "4. Ludwig Boltzmann", "theory": "Thermodynamic Time (Arrow of Time)", "text": "The unidirectional flow of time is driven by increasing entropy.", "source": "Lectures on Gas Theory (1896)"},
            {"name": "5. Stephen Hawking", "theory": "Cosmological Time & Big Bang", "text": "Time began with the Big Bang and may evolve into imaginary time in quantum frameworks.", "source": "A Brief History of Time (1988)"},
            {"name": "6. Ilya Prigogine", "theory": "Irreversibility and Chaos", "text": "In complex systems, time evolution is irreversible.", "source": "The End of Certainty (1996)"},
            {"name": "7. Carlo Rovelli", "theory": "Loop Quantum Gravity & Thermal Time", "text": "Time is not fundamental at the quantum level; it is a macro-level emergent illusion.", "source": "The Order of Time (2017)"},
            {"name": "8. Julian Barbour", "theory": "The End of Time", "text": "Time does not physically flow; each 'now' is an independent timeless configuration.", "source": "The End of Time (1999)"},
            {"name": "9. Max Planck", "theory": "Planck Time", "text": "The fundamental quantum limit of time measurement (10^-43 seconds).", "source": "Quantum Theory Compilations (1899)"},
            {"name": "10. John Wheeler", "theory": "Quantum Foam", "text": "At Planck scales, spacetime smooth geometry dissolves into turbulent quantum foam.", "source": "Geometrodynamics (1962)"},
            {"name": "11. Arthur Eddington", "theory": "Arrow of Time", "text": "Entropy increase distinguishes past from future direction.", "source": "The Nature of the Physical World (1928)"},
            {"name": "12. Erwin Schrödinger", "theory": "Quantum Wave Equation", "text": "Mathematical modeling of quantum states evolving over time.", "source": "Annalen der Physik (1926)"},
            {"name": "13. Hendrik Lorentz", "theory": "Lorentz Transformations", "text": "Mathematical formulation of time dilation in moving frames before relativity.", "source": "Electromagnetic Phenomena (1904)"},
            {"name": "14. Henri Poincaré", "theory": "Conventionality of Simultaneity", "text": "Time synchronization depends on signal propagation conventions.", "source": "Science and Hypothesis (1902)"},
            {"name": "15. Kurt Gödel", "theory": "Gödel Universe & Closed Timelike Curves", "text": "Relativity equations allow closed time loops in rotating universes, making time travel theoretically possible.", "source": "Einstein's Field Equations Solutions (1949)"}
        ],
        "legal_full": """
        ### ⚖️ LEGAL PROTECTION AND COPYRIGHT NOTICE
        
        1. *Informational Purpose Only:* Provided for personal education, research, and contemplation.
        2. *Prohibition of Commercial Use:* Commercial sale or monetization is strictly prohibited.
        3. *Copy Protection:* Protected under copyright laws; scraping or unauthorized copying is prohibited.
        """
    }
}

# -----------------------------------------------------------------------------
# 3. KENAR ÇUBUĞU (SIDEBAR) VE NAVİGASYON
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🌐 Dil / Language")
    lang_choice = st.radio(
        "Seçiniz / Select:",
        options=["TR", "EN"],
        format_func=lambda x: "🇹🇷 Türkçe" if x == "TR" else "🇬🇧 English",
        horizontal=True
    )
    
    t = DATA[lang_choice]
    
    st.markdown("---")
    st.markdown(f"### 📑 {t['nav_title']}")
    selected_section = st.radio(
        label="Navigation",
        options=t["sections"],
        label_visibility="collapsed"
    )
    
    # İstediğiniz uyku modu bilgi notu eklendi
    st.markdown("---")
    st.info(
        "💡 *Not:* Bu web uygulaması ücretsiz sunucularda barındırılmaktadır. "
        "Uzun süre işlem yapılmadığında uygulama uyku moduna geçebilir "
        "(ekranda 'Zzzz' simgesi çıkabilir).\n\n"
        "💤 Eğer böyle bir ekranla karşılaşırsanız, ekranda beliren mavi renkli "
        "*'Yes, get this app back up!'* butonuna tıklayın ve uygulamanın "
        "yeniden uyanması için 15-30 saniye bekleyin."
    )
    
    st.markdown("---")
    st.warning(t["legal_short"])

# -----------------------------------------------------------------------------
# 4. ANA BAŞLIK ALANI
# -----------------------------------------------------------------------------
st.title(t["app_title"])
st.markdown(f"*{t['app_subtitle']}*")
st.markdown("---")

def render_card(title, text, source):
    st.markdown(f"""
    <div class="info-card">
        <div class="card-title">{title}</div>
        <div class="card-text">{text}</div>
        <div class="card-source">📚 {source}</div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. BÖLÜM İÇERİKLERİNİN GÖSTERİMİ
# -----------------------------------------------------------------------------
sec_index = t["sections"].index(selected_section)

if sec_index == 0:
    st.header(t["sec1_title"])
    for item in t["sec1_content"]:
        render_card(item["title"], item["text"], item["source"])

elif sec_index == 1:
    st.header(t["sec2_title"])
    for item in t["sec2_content"]:
        render_card(item["title"], item["text"], item["source"])

elif sec_index == 2:
    st.header(t["sections"][2])
    for v in t["verses"]:
        render_card(v["surah"], f"“{v['text']}”", v["source"])

elif sec_index == 3:
    st.header(t["sections"][3])
    for h in t["hadiths"]:
        render_card(h["title"], f"“{h['text']}”", h["source"])

elif sec_index == 4:
    st.header(t["sections"][4])
    for b in t["bediuzzaman"]:
        render_card(b["title"], b["text"], b["source"])

elif sec_index == 5:
    st.header(t["sections"][5])
    for s in t["saints"]:
        render_card(s["name"], f"“{s['quote']}”", s["source"])

elif sec_index == 6:
    st.header(t["sections"][6])
    for sc in t["scientists"]:
        render_card(f"{sc['name']} — {sc['theory']}", sc['text'], sc['source'])

elif sec_index == 7:
    st.markdown(t["legal_full"])

# -----------------------------------------------------------------------------
# 6. ALT BİLGİ VE HUKUKİ KORUMA ŞERİDİ
# -----------------------------------------------------------------------------
st.markdown(f"""
<div class="legal-banner">
    {t['legal_short']} <br>
    <strong>© 2026 - Tüm Hakları Saklıdır / All Rights Reserved | Kopyalama Korumalı Sistem (Copy-Protected)</strong>
</div>
""", unsafe_allow_html=True)