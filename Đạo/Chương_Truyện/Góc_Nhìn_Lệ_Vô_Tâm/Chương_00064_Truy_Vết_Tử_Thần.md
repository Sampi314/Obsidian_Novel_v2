<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00005_Ván_Cờ_Huyết_Độc.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a id="next-chapter-link" href="Chương_00007_Dưới_Bóng_Hắc_Sa.html">Chương Sau ➡️</a></td>
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
<li style="padding: 5px; "><a href="Chương_00003_Mệnh_Lệnh_Bóng_Tối.html">Chương 3: Mệnh Lệnh Bóng Tối</a></li>
<li style="padding: 5px; "><a href="Chương_00004_Thí_Nghiệm_Máu.html">Chương 4: Thí Nghiệm Máu</a></li>
<li style="padding: 5px; "><a href="Chương_00005_Ván_Cờ_Huyết_Độc.html">Chương 5: Ván Cờ Huyết Độc</a></li>
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00006_Truy_Vết_Tử_Thần.html">Chương 6: Truy Vết Tử Thần</a></li>
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
    var isStopped = false;

    // Elements to read
    var contentElements = [];

    // Next chapter URL
    var nextChapterUrl = "Chương_00007_Dưới_Bóng_Hắc_Sa.html";

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
# Chương 6: Truy Vết Tử Thần

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Lệ Vô Tâm](../../Nhân_Vật/Lệ_Vô_Tâm.md)
**Nhân vật liên quan:** [Huyết Vệ](../../Nhân_Vật/Huyết_Vệ.md)
**Địa điểm:** Rìa Rừng Huyết Độc - Giáp ranh Tây Mạc.
**Thời điểm:** Song song với hành trình tiến vào Tây Mạc của nhóm nhân vật chính.
**Giao Điểm Cốt Truyện:** [Chương 10: Sa Mạc Tử Thần](../Góc_Nhìn_Chính/Chương_00010_Sa_Mạc_Tử_Thần.md).

---

Gió nóng từ phía Tây thổi tới, mang theo vị mặn chát của cát và mùi hôi thối đặc trưng của những xác chết khô.

Ta đứng trên một mỏm đá cao, nhìn về phía chân trời xa xăm, nơi màu xanh của [Rừng Huyết Độc](../../Kỳ_Vật/Rừng_Huyết_Độc.md) dần bị nuốt chững bởi biển cát vàng mênh mông của Tây Mạc. Tà áo bào đỏ thẫm của ta bay phần phật, tựa như một ngọn lửa ma quái giữa ranh giới của sự sống và cái chết.

"Thánh Tử."

Một bóng đen xuất hiện sau lưng ta, quỳ một gối xuống. Hắn là thủ lĩnh đội Huyết Vệ, những con chó săn trung thành nhất mà ta đã đào tạo từ trong vũng máu của Huyết Trì.

"Nói." Ta không quay đầu lại, mắt vẫn dán chặt vào hướng Tây.

"Thiên Tinh Cổ đã gửi tín hiệu về. Mục tiêu... đã tiến vào Tây Mạc."

Ta nhếch mép cười. *Tây Mạc sao?* Một lựa chọn thú vị. Hai con chuột nhắt kia, một kẻ bị thương, một kẻ mang theo bí mật của Vạn Độc Môn, lại dám lao đầu vào vùng đất chết chóc đó.

"Bọn chúng đi tìm cái gì?" Ta hỏi, giọng nói lạnh lùng nhưng ẩn chứa sự tò mò.

"Thuộc hạ vô năng," tên Huyết Vệ cúi đầu thấp hơn, giọng run rẩy. "Tín hiệu bị nhiễu loạn bởi bão cát. Nhưng hướng đi của chúng... dường như nhắm tới phế tích của Hoàng Sa Quốc cổ đại."

*Hoàng Sa Quốc...*

Cái tên này gợi lên trong ta một vài ký ức vụn vặt từ những cuốn cổ thư trong Tàng Thư Các của tông môn. Một vương quốc đã bị chôn vùi dưới cát từ hàng ngàn năm trước, nơi được đồn đại là ẩn chứa [Long Cốt](../../Kỳ_Vật/Long_Cốt.md) – long mạch của cả vùng Tây Mạc. Nếu bọn chúng thực sự nhắm đến đó...

Ta xòe bàn tay phải ra. Một con rết nhỏ màu đỏ tía – con *Thiên Tinh Cổ* cái – đang ngọ nguậy trong lòng bàn tay. Nó phát ra những tiếng rít khe khẽ, truyền tải sự lo lắng và bất an từ con đực đang bám theo mục tiêu.

"Bão cát... Sa Hồn... Và cả những thứ kinh khủng hơn đang ngủ say dưới lớp cát đó," ta lẩm bẩm.

"Thánh Tử, chúng ta có nên đuổi theo không?" Tên Huyết Vệ rụt rè hỏi.

Ta quay phắt lại, ánh mắt sắc như dao găm xoáy vào hắn.

"Đuổi theo? Ngươi muốn dẫn đám huynh đệ của ngươi đi làm mồi cho Sa Hồn sao?"

Tên Huyết Vệ rùng mình, vội vàng dập đầu xuống đất. "Thuộc hạ không dám!"

Ta hừ lạnh, thu hồi Thiên Tinh Cổ vào tay áo. "Kẻ khôn ngoan không bao giờ lao đầu vào chỗ chết. Tây Mạc là nơi tử địa, nhưng cũng là cái lồng tự nhiên hoàn hảo nhất. Bọn chúng vào được, chưa chắc đã ra được."

Ta bước xuống khỏi mỏm đá, đi về phía doanh trại tạm thời dựng bên bìa rừng.

"Truyền lệnh xuống," giọng ta vang lên, trầm thấp và đầy uy quyền. "Phong tỏa toàn bộ các lối ra từ Tây Mạc dẫn về Nam Cương. Rải [Huyết Độc Phấn](../../Kỳ_Vật/Huyết_Độc_Phấn.md) dọc theo biên giới rừng. Ta muốn biến nơi này thành một cái lưới không lối thoát."

"Rõ!" Tên Huyết Vệ hô to, rồi biến mất vào bóng tối như chưa từng tồn tại.

Ta ngồi xuống chiếc ghế da hổ trong lều, rót một chén rượu huyết bồ đào. Màu rượu đỏ thẫm sóng sánh như máu tươi.

Lâm Phong... Diệp Tĩnh Sương...

Các ngươi cứ việc vùng vẫy trong biển cát đó đi. Nếu các ngươi chết trong đó, coi như ta đỡ tốn công sức. Còn nếu các ngươi may mắn sống sót trở về...

Ta nâng chén rượu lên, nhìn hình ảnh phản chiếu méo mó của mình trong đó. Đôi mắt ta ánh lên tia nhìn tàn độc.

...Thì ta sẽ là người đầu tiên chào đón các ngươi ở cửa địa ngục.

"Đợi đấy," ta thì thầm, uống cạn chén rượu. "Trò chơi mèo vờn chuột, giờ mới thực sự bắt đầu."
