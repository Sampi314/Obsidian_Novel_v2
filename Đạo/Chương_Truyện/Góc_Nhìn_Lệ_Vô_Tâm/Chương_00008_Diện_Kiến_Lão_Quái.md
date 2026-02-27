<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00007_Huyết_Nguyệt_Sát_Cơ.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a id="next-chapter-link" href="Chương_00009_Bể_Dược_Độc.html">Chương Sau ➡️</a></td>
</tr>
</table>
<details style="margin-top: 10px;">
<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>
<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">
<li style="padding: 5px; "><a href="Chương_00001_Đường_Đến_Thánh_Vị.html">Chương 1: Đường Đến Thánh Vị</a></li>
<li style="padding: 5px; "><a href="Chương_00002_Hậu_Quả_Sinh_Tồn.html">Chương 2: Hậu Quả Sinh Tồn</a></li>
<li style="padding: 5px; "><a href="Chương_00003_Bài_Học_Vô_Cảm.html">Chương 3: Bài Học Vô Cảm</a></li>
<li style="padding: 5px; "><a href="Chương_00004_Sự_Phản_Bội_Đầu_Tiên.html">Chương 4: Sự Phản Bội Đầu Tiên</a></li>
<li style="padding: 5px; "><a href="Chương_00005_Bóng_Tối_Cô_Độc.html">Chương 5: Bóng Tối Cô Độc</a></li>
<li style="padding: 5px; "><a href="Chương_00006_Thử_Thách_Vạn_Độc.html">Chương 6: Thử Thách Vạn Độc</a></li>
<li style="padding: 5px; "><a href="Chương_00007_Huyết_Nguyệt_Sát_Cơ.html">Chương 7: Huyết Nguyệt Sát Cơ</a></li>
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00008_Diện_Kiến_Lão_Quái.html">Chương 8: Diện Kiến Lão Quái</a></li>
<li style="padding: 5px; "><a href="Chương_00031_Huyết_Độc_Phiến.html">Chương 31: Huyết Độc Phiến</a></li>
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
    var isStopped = false;

    // Elements to read
    var contentElements = [];

    // Next chapter URL
    var nextChapterUrl = "Chương_00009_Bể_Dược_Độc.html";

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

        isStopped = false;

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
        if (isStopped) return;

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
            if (isStopped) return;

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
            if (isStopped) return;

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
        isStopped = true;
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
        isStopped = true;
        synth.cancel();
    };
</script>

</div>
<!-- NAVIGATION_END -->
# Chương 8: Diện Kiến Lão Quái

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Lệ Vô Tâm](../../Nhân_Vật/Lệ_Vô_Tâm.md)
**Địa điểm:** Vạn Độc Cốc (Động phủ Độc Cô Lão Quái).
**Thời điểm:** 6 tháng sau Huyết Trì (Hữu Tâm 13.5 tuổi).
**Giao Điểm Cốt Truyện:** Tuyến độc lập (Quá khứ).

---

Sáu tháng.
Sáu tháng kể từ ngày ta trở thành kẻ sống sót duy nhất của Huyết Trì.

Sáu tháng ta sống như một con chuột trong hang đá, ăn thịt chuột sống, uống nước đọng, và giết bất cứ thứ gì dám bén mảng đến gần nơi trú ẩn của ta. Ta không còn là Hữu Tâm ngây thơ ngày nào. Ta đã học được cách phân biệt tiếng bước chân của kẻ thù, cách nhận biết các loại độc dược cơ bản qua mùi, và quan trọng nhất: cách giết người nhanh nhất mà không cần vũ khí.

Hôm nay, một Huyết Vệ mặc giáp đỏ xuất hiện trước cửa hang của ta. Hắn không nói gì, chỉ ném cho ta một bộ áo choàng đen và ra hiệu đi theo.

Ta biết ngày này sẽ đến. Độc Cô Lão Quái muốn gặp "tác phẩm" của mình.

Động phủ của lão nằm sâu trong lòng núi, nơi mà ánh sáng mặt trời không bao giờ chạm tới. Càng đi vào sâu, không khí càng trở nên đặc quánh, nồng nặc mùi lưu huỳnh và thảo dược thối rữa. Ta nhìn thấy những cái lồng sắt treo lơ lửng trên trần hang, bên trong nhốt đủ loại sinh vật kỳ dị: những con rắn hai đầu, những con cóc to bằng cái thúng, và cả... những con người bị biến dạng.

Có kẻ mọc đầy vảy như cá, có kẻ da thịt thối rữa lộ cả xương trắng, có kẻ thì tứ chi teo tóp như cành củi khô. Tất cả bọn họ đều nhìn ta với ánh mắt trống rỗng, vô hồn.

"Sợ sao?"

Giọng nói khàn đục vang lên từ trong bóng tối. Ta rùng mình, không phải vì sợ, mà vì áp lực vô hình đè nặng lên vai.

Độc Cô Lão Quái ngồi trên một chiếc ghế làm từ xương cốt của một loài yêu thú khổng lồ nào đó. Lão gầy gò, da nhăn nheo như vỏ cây cổ thụ, đôi mắt hẹp dài ánh lên tia nhìn sắc lạnh như dao cạo.

Ta quỳ xuống, dập đầu sát đất. "Đệ tử tham kiến Sư Tôn."

"Sư Tôn?" Lão cười khẩy, tiếng cười như tiếng móng tay cào lên bảng đá. "Ngươi chưa xứng đáng gọi ta là Sư Tôn. Ngươi chỉ là một con tốt thí nghiệm may mắn sống sót mà thôi."

Ta im lặng. Ta biết lão nói đúng. Ở Vạn Độc Môn, mạng sống rẻ mạt như cỏ rác.

Lão phất tay. Một cái vạc lớn đặt giữa hang bỗng nhiên sôi sùng sục. Chất lỏng bên trong có màu xanh đen, tỏa ra làn khói tím ngắt.

"Nhảy vào," lão ra lệnh ngắn gọn.

Ta ngẩng đầu nhìn cái vạc. Nhiệt độ tỏa ra từ đó đủ để làm cháy sém lông mày ta. Mùi độc dược xộc vào mũi khiến ta choáng váng.

"Sợ chết?" Lão Quái nhếch mép. "Nếu không dám, ngươi có thể quay lại làm thức ăn cho lũ rắn ngoài kia."

Ta đứng dậy, cởi bỏ bộ áo choàng đen, để lộ cơ thể gầy gò đầy sẹo. Ta bước đến bên cái vạc, không một chút do dự.

Chết? Ta đã chết một lần ở Huyết Trì rồi. Cái chết bây giờ đối với ta chẳng qua chỉ là một giấc ngủ dài.

Ta trèo lên thành vạc, nhắm mắt lại và nhảy xuống.

*Xèo!*

Da thịt ta như bị tẩm axit. Cơn đau khủng khiếp ập đến, xé toạc từng dây thần kinh. Ta muốn hét lên, nhưng cổ họng ta như bị bóp nghẹt. Ta vùng vẫy trong tuyệt vọng, cảm nhận từng tấc da thịt mình đang tan chảy.

Nhưng rồi, một luồng khí lạnh buốt chạy dọc sống lưng ta, đối chọi với sức nóng thiêu đốt của độc dược. Đó là luồng khí ta hấp thụ được từ con rết ở Huyết Trì. Hai luồng khí nóng lạnh giao tranh trong cơ thể ta, biến ta thành một bãi chiến trường.

Ta cắn chặt môi đến bật máu, cố gắng giữ cho mình tỉnh táo. Ta không thể chết ở đây. Ta phải sống. Ta phải sống để trả thù cho Tiểu Lan, trả thù cho chính bản thân mình.

Qua làn khói mờ ảo, ta thấy Độc Cô Lão Quái đang nhìn mình chằm chằm. Trong ánh mắt lão không có sự thương xót, chỉ có sự tò mò của một kẻ điên đang quan sát thí nghiệm của mình.

"Tốt," lão lầm bầm. "Ý chí khá lắm. Xem ra ngươi chịu được 'Vạn Độc Phệ Thân' cấp một."

Ta không nghe rõ lão nói gì nữa. Ý thức ta dần chìm vào bóng tối. Điều cuối cùng ta nhớ được là nụ cười méo mó trên khuôn mặt lão già ấy.

Địa ngục thực sự... bây giờ mới bắt đầu.
