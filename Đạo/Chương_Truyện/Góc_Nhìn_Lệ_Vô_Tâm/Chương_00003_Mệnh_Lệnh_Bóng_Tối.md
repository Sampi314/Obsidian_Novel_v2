<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00002_8_Thanh_Trừng_Nội_Bộ.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a id="next-chapter-link" href="Chương_00004_Thí_Nghiệm_Máu.html">Chương Sau ➡️</a></td>
</tr>
</table>
<details style="margin-top: 10px;">
<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>
<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">
<li style="padding: 5px; "><a href="Chương_00001_Đường_Đến_Thánh_Vị.html">Chương 1: Đường Đến Thánh Vị</a></li>
<li style="padding: 5px; "><a href="Chương_00002_Huyết_Độc_Phiến.html">Chương 2: Huyết Độc Phiến</a></li>
<li style="padding: 5px; "><a href="Chương_00002_2_Bẫy_Rập_Rừng_Sương.html">Chương 2.2: Bẫy Rập Rừng Sương</a></li>
<li style="padding: 5px; "><a href="Chương_00002_5_Diệt_Môn_Chi_Họa.html">Chương 2.5: Diệt Môn Chi Họa</a></li>
<li style="padding: 5px; "><a href="Chương_00002_8_Thanh_Trừng_Nội_Bộ.html">Chương 2.8: Thanh Trừng Nội Bộ</a></li>
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00003_Mệnh_Lệnh_Bóng_Tối.html">Chương 3: Mệnh Lệnh Bóng Tối</a></li>
<li style="padding: 5px; "><a href="Chương_00004_Thí_Nghiệm_Máu.html">Chương 4: Thí Nghiệm Máu</a></li>
<li style="padding: 5px; "><a href="Chương_00005_Ván_Cờ_Huyết_Độc.html">Chương 5: Ván Cờ Huyết Độc</a></li>
<li style="padding: 5px; "><a href="Chương_00006_Truy_Vết_Tử_Thần.html">Chương 6: Truy Vết Tử Thần</a></li>
<li style="padding: 5px; "><a href="Chương_00007_Dưới_Bóng_Hắc_Sa.html">Chương 7: Dưới Bóng Hắc Sa</a></li>
<li style="padding: 5px; "><a href="Chương_00008_Huyết_Tế_Sa_Mạc.html">Chương 8: Huyết Tế Sa Mạc</a></li>
<li style="padding: 5px; "><a href="Chương_00009_Sát_Ý_Rừng_Gai.html">Chương 9: Sát Ý Rừng Gai</a></li>
<li style="padding: 5px; "><a href="Chương_00010_Mạng_Lưới_Tử_Thần.html">Chương 10: Mạng Lưới Tử Thần</a></li>
</ul>
</details>
<div style="margin-top: 15px; border-top: 1px solid #ccc; padding-top: 10px;">
  <strong>🎧 Nghe Chương Này:</strong>
  <br>
  <button id="btn-play" onclick="startReading()" style="cursor: pointer; padding: 5px 10px; margin: 5px;">▶️ Đọc</button>
  <button id="btn-pause" onclick="pauseReading()" style="cursor: pointer; padding: 5px 10px; margin: 5px; display: none;">⏸️ Tạm Dừng</button>
  <button id="btn-resume" onclick="resumeReading()" style="cursor: pointer; padding: 5px 10px; margin: 5px; display: none;">⏯️ Tiếp Tục</button>
  <button id="btn-stop" onclick="stopReading()" style="cursor: pointer; padding: 5px 10px; margin: 5px; display: none;">⏹️ Dừng</button>
</div>

<script>
    var synth = window.speechSynthesis;
    var currentUtterance = null;
    var readingQueue = [];
    var currentIndex = 0;
    var isPaused = false;

    // Elements to read
    var contentElements = [];

    // Next chapter URL
    var nextChapterUrl = "Chương_00004_Thí_Nghiệm_Máu.html";

    function getReadableElements() {
        // Collect all paragraph-like elements in the body
        // Filter out navigation, headers, footers, and specific unwanted text
        var all = document.body.querySelectorAll('p, h1, h2, h3, h4, h5, h6, li, blockquote');
        var readable = [];

        for (var i = 0; i < all.length; i++) {
            var el = all[i];

            // Skip navigation block
            if (el.closest('#chapter-navigation')) continue;

            // Skip invisible elements
            if (el.offsetParent === null) continue;

            var text = el.innerText.trim();
            if (text.length === 0) continue;

            // Skip specific unwanted text
            if (text.includes("Obsidian_Novel_v2")) continue;
            if (text.includes("Mục Lục Tổng Hợp")) continue;

            readable.push(el);
        }
        return readable;
    }

    function startReading() {
        if (synth.speaking && !isPaused) return;

        // Reset controls
        document.getElementById("btn-play").style.display = "none";
        document.getElementById("btn-pause").style.display = "inline-block";
        document.getElementById("btn-resume").style.display = "none";
        document.getElementById("btn-stop").style.display = "inline-block";

        contentElements = getReadableElements();

        if (currentIndex >= contentElements.length) {
            currentIndex = 0; // Restart if finished
        }

        readNextChunk();
    }

    function readNextChunk() {
        if (currentIndex >= contentElements.length) {
            // Finished reading the chapter
            stopReading();

            // Auto-advance to next chapter if available
            if (nextChapterUrl && nextChapterUrl !== "#") {
                // Add autoplay param
                var separator = nextChapterUrl.includes('?') ? '&' : '?';
                window.location.href = nextChapterUrl + separator + 'autoplay=true';
            }
            return;
        }

        var el = contentElements[currentIndex];

        // Highlight current element
        el.style.backgroundColor = "#e6f7ff";
        el.style.borderLeft = "4px solid #1890ff";
        el.style.paddingLeft = "10px";
        el.scrollIntoView({behavior: "smooth", block: "center"});

        var text = el.innerText;
        var utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = "vi-VN";

        utterance.onend = function() {
            // Remove highlight
            el.style.backgroundColor = "";
            el.style.borderLeft = "";
            el.style.paddingLeft = "";

            currentIndex++;
            if (!isPaused && synth.speaking === false) {
                 readNextChunk();
            }
        };

        utterance.onerror = function(event) {
            console.error("Speech error", event);
            // Try to skip to next chunk on error
            el.style.backgroundColor = "";
            el.style.borderLeft = "";
            el.style.paddingLeft = "";
            currentIndex++;
            readNextChunk();
        };

        currentUtterance = utterance;
        synth.speak(utterance);
    }

    function pauseReading() {
        if (synth.speaking && !isPaused) {
            synth.pause();
            isPaused = true;
            document.getElementById("btn-pause").style.display = "none";
            document.getElementById("btn-resume").style.display = "inline-block";
        }
    }

    function resumeReading() {
        if (isPaused) {
            synth.resume();
            isPaused = false;
            document.getElementById("btn-pause").style.display = "inline-block";
            document.getElementById("btn-resume").style.display = "none";
        } else if (!synth.speaking && currentIndex < contentElements.length) {
            // Resume from stop or clean state
            startReading();
        }
    }

    function stopReading() {
        synth.cancel();
        isPaused = false;

        // Clean up highlights
        if (contentElements.length > 0 && currentIndex < contentElements.length) {
            var el = contentElements[currentIndex];
            if (el) {
                el.style.backgroundColor = "";
                el.style.borderLeft = "";
                el.style.paddingLeft = "";
            }
        }

        currentIndex = 0;

        document.getElementById("btn-play").style.display = "inline-block";
        document.getElementById("btn-pause").style.display = "none";
        document.getElementById("btn-resume").style.display = "none";
        document.getElementById("btn-stop").style.display = "none";
    }

    // Auto-play check
    window.onload = function() {
        var urlParams = new URLSearchParams(window.location.search);
        if (urlParams.get('autoplay') === 'true') {
            // Delay slightly to ensure voices are loaded
            setTimeout(startReading, 1000);
        }
    };

    // Handle page unload to stop speech
    window.onbeforeunload = function() {
        synth.cancel();
    };
</script>

</div>
<!-- NAVIGATION_END -->
# Chương 3: Mệnh Lệnh Bóng Tối

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Lệ Vô Tâm](../../Nhân_Vật/Lệ_Vô_Tâm.md)
**Địa điểm:** Vạn Độc Môn (Đại Điện) và Đường đến Thôn Lạc Diệp.
**Thời điểm:** Hiện tại (Bắt đầu "Huyết Độc Chi Họa").
**Giao Điểm Cốt Truyện:** Dẫn nhập vào sự kiện Thôn Lạc Diệp.

---

Mười năm trôi qua.

Thời gian đối với phàm nhân là sự lão hóa, nhưng đối với tu sĩ, nó là sự tích lũy. Ta, Lệ Vô Tâm, giờ đây không còn là đứa trẻ gầy gò năm nào. Ta đứng trên đỉnh Vạn Độc Phong, gió lộng thổi tung tà áo bào đen thêu hình rết độc. Dưới chân ta, hàng ngàn đệ tử Vạn Độc Môn đang quỳ rạp, không ai dám ngẩng đầu nhìn thẳng vào mắt ta.

Trúc Cơ Viên Mãn. Chỉ còn một bước nữa là Kết Đan.

Nhưng bước chân này khó như lên trời. Ta cần một cơ hội, một sự đột phá sinh tử.

"Thánh Tử," một tên đệ tử áo đen cung kính bước tới, cắt ngang dòng suy nghĩ của ta. "Sư tôn có lệnh triệu kiến."

Ta thu lại luồng khí tức âm hàn, phe phẩy chiếc [Huyết Độc Phiến](../../Luyện_Khí/Huyết_Độc_Phiến.md), thong thả bước về phía đại điện.

***

Đại điện Vạn Độc Môn tối tăm và ẩm thấp, ngập tràn mùi hương trầm trộn lẫn mùi xác thối. Độc Cô Lão Quái ngồi trên ngai xương, đôi mắt xanh lục lập lòe như ma trơi trong hốc mắt sâu hoắm.

"Vô Tâm tham kiến sư tôn." Ta chắp tay, cúi đầu vừa đủ lễ độ.

"Vô Tâm," giọng lão khàn đặc, vang vọng khắp đại điện trống trải. "Huyết Thần Độc đã hoàn thiện chưa?"

"Bẩm sư tôn, đã đến giai đoạn cuối cùng. Chỉ cần một cuộc thử nghiệm thực tế trên diện rộng để kiểm chứng khả năng lây lan và biến đổi."

Độc Cô Lão Quái gật đầu hài lòng. Lão ném cho ta một tấm thẻ ngọc màu huyết dụ.

"Thôn Lạc Diệp. Một ngôi làng nhỏ ở rìa Vĩnh Hằng Sâm Lâm. Địa thế kín đáo, linh khí loãng, ít người chú ý. Ngươi hãy đến đó, biến ngôi làng đó thành sân chơi của ngươi."

Ta bắt lấy tấm thẻ ngọc, cảm nhận được luồng tin tức chạy thẳng vào não bộ. Bản đồ, danh sách dân cư, và... một mật lệnh.

*“Nếu thành công, Huyết Tướng sẽ là vũ khí tối thượng để ta san bằng Dược Vương Cốc. Nếu thất bại... ngươi tự biết hậu quả.”*

"Đệ tử đã rõ," ta đáp, khóe môi nhếch lên một nụ cười lạnh.

"Còn một việc nữa," lão già nheo mắt, ánh nhìn sắc lẹm như muốn xuyên thấu tâm can ta. "Gần đây, lũ chó săn của Chính Đạo đang đánh hơi được mùi gì đó. Đặc biệt là đám kiếm tu Cửu Hoa và đám thầy thuốc giả nhân giả nghĩa Dược Vương Cốc. Nếu gặp chúng..."

"Giết không tha," ta tiếp lời, giọng điệu dứt khoát.

"Đi đi."

***

Ta rời khỏi Vạn Độc Môn ngay trong đêm.

Thôn Lạc Diệp. Cái tên nghe thật thê lương, như báo trước số phận của những kẻ sống ở đó. Ta không hề cảm thấy tội lỗi. Trong mắt ta, bọn họ chỉ là những con kiến, và cái chết của họ sẽ lót đường cho đại nghiệp của ta.

Ta cưỡi trên lưng một con Hắc Vũ Điêu, bay lướt qua những cánh rừng bạt ngàn của Nam Cương. Gió đêm quất vào mặt lạnh buốt, nhưng máu trong người ta lại đang sôi lên sùng sục.

Ta cần máu của Huyết Tướng để luyện hóa đan điền, đột phá Kim Đan. Ta cần sự hỗn loạn để che giấu tham vọng của riêng mình.

Khi ánh bình minh vừa ló dạng phía chân trời, ta đã nhìn thấy những mái nhà tranh lấp ló dưới tán cây cổ thụ của Thôn Lạc Diệp. Ngôi làng yên bình, khói bếp bay lên nghi ngút, tiếng gà gáy văng vẳng xa xa.

Thật yên bình. Thật... mong manh.

Ta đáp xuống một ngọn đồi gần đó, thu hồi Hắc Vũ Điêu. Ta lấy ra một chiếc lọ nhỏ từ trong tay áo. Bên trong là một con bọ cánh cứng màu đỏ rực. [Huyết Thần Độc](../../Kỳ_Vật/Huyết_Thần_Độc.md) dạng ấu trùng.

"Bắt đầu thôi," ta thì thầm, thả con bọ bay về phía nguồn nước của ngôi làng.

Đường đến thánh vị, trải đầy xương trắng và máu tươi. Và Lạc Diệp Thôn... sẽ là nấc thang tiếp theo của ta.

Ta quay người, bước về phía căn hầm bí mật mà các đệ tử tiền trạm đã chuẩn bị sẵn. Ở đó, những "vật liệu" thí nghiệm đang chờ đợi ta.

*Hữu Tâm đã chết. Giờ đây, chỉ còn lại Lệ Vô Tâm.*
