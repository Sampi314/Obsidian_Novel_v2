<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00002_2_Bẫy_Rập_Rừng_Sương.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a id="next-chapter-link" href="Chương_00002_8_Thanh_Trừng_Nội_Bộ.html">Chương Sau ➡️</a></td>
</tr>
</table>
<details style="margin-top: 10px;">
<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>
<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">
<li style="padding: 5px; "><a href="Chương_00001_Đường_Đến_Thánh_Vị.html">Chương 1: Đường Đến Thánh Vị</a></li>
<li style="padding: 5px; "><a href="Chương_00002_Huyết_Độc_Phiến.html">Chương 2: Huyết Độc Phiến</a></li>
<li style="padding: 5px; "><a href="Chương_00002_2_Bẫy_Rập_Rừng_Sương.html">Chương 2.2: Bẫy Rập Rừng Sương</a></li>
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00002_5_Diệt_Môn_Chi_Họa.html">Chương 2.5: Diệt Môn Chi Họa</a></li>
<li style="padding: 5px; "><a href="Chương_00002_8_Thanh_Trừng_Nội_Bộ.html">Chương 2.8: Thanh Trừng Nội Bộ</a></li>
<li style="padding: 5px; "><a href="Chương_00003_Mệnh_Lệnh_Bóng_Tối.html">Chương 3: Mệnh Lệnh Bóng Tối</a></li>
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
    var isStopped = false;

    // Elements to read
    var contentElements = [];

    // Next chapter URL
    var nextChapterUrl = "Chương_00002_8_Thanh_Trừng_Nội_Bộ.html";

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
# Chương 2.5: Diệt Môn Chi Họa

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Lệ Vô Tâm](../../Nhân_Vật/Lệ_Vô_Tâm.md)
**Địa điểm:** Lý Gia (Biên giới Nam Cương).
**Thời điểm:** 8 năm trước (Lệ Vô Tâm 20 tuổi).
**Giao Điểm Cốt Truyện:** Tuyến độc lập (Quá khứ).

---

Ánh trăng đêm rằm tròn vành vạnh, soi rọi xuống tòa phủ đệ nguy nga của Lý Gia, gia tộc tu tiên giàu có nhất vùng biên giới Nam Cương. Tiếng đàn sáo réo rắt, tiếng cười nói rộn ràng vọng ra từ đại sảnh, nơi đang diễn ra yến tiệc mừng thọ lão tổ Lý Gia tròn 200 tuổi.

Ta đứng trên mái ngói cong vút của cổng chính, chiếc [Huyết Độc Phiến](../../Luyện_Khí/Huyết_Độc_Phiến.md) phe phẩy trên tay. Gió đêm thổi tung tà áo tím than thêu hoa văn độc trùng, nhưng không thể xua tan được mùi rượu nồng nặc và... mùi chết chóc đang đến gần.

"Lý Gia..." Ta lẩm bẩm, khóe môi nhếch lên một nụ cười lạnh. "Hưởng lạc thế là đủ rồi."

Lý do ta đến đây? Đơn giản thôi. Ba tháng trước, đoàn xe chở cống phẩm của Vạn Độc Môn đi ngang qua địa bàn Lý Gia đã bị chặn lại. Lũ ngu xuẩn này dám đòi tiền mãi lộ, thậm chí còn đánh trọng thương đệ tử áp tải.

Độc Cô Lão Quái không nói gì, chỉ ném cho ta một cái nhìn sắc lẹm: *"Vô Tâm, thể diện của tông môn, ngươi tự biết phải làm gì."*

Thể diện. Hai chữ đó nặng ngàn cân. Và cái giá để rửa sạch nó phải trả bằng máu.

Ta nhảy xuống sân trước, nhẹ nhàng như một chiếc lá rơi. Hai tên lính gác cổng còn chưa kịp nhìn thấy bóng dáng ai đã ngã gục, cổ họng trào máu đen.

"Ai đó?!"

Tiếng hô hoán vang lên. Một đội tuần tra mười người lao tới, đao kiếm sáng loáng.

"Khách không mời mà đến," ta đáp, giọng bình thản nhưng vang vọng khắp sân. "Mang quà mừng thọ đến cho Lý lão tổ đây."

Ta phất tay áo. Một làn khói màu hồng phấn bay ra, thơm ngát mùi hoa đào.

[Mê Hồn Hương](../../Kỳ_Vật/Mê_Hồn_Hương.md).

Đám lính hít phải hương thơm, mắt đờ đẫn, tay buông lỏng vũ khí. Chúng bắt đầu cười ngây dại, rồi quay sang chém giết lẫn nhau trong cơn ảo giác. Tiếng la hét thảm thiết xé toạc màn đêm yên tĩnh.

"Dừng tay!"

Một tiếng quát uy lực vang lên từ đại sảnh. Một lão già râu tóc bạc phơ, mặc áo gấm thêu rồng, bay vút ra. Theo sau là hàng chục tu sĩ Trúc Cơ kỳ của Lý Gia.

Lý Thiên Bá - Gia chủ Lý Gia, Trúc Cơ Hậu Kỳ.

"Ngươi là kẻ nào? Dám đến Lý Gia ta làm loạn?" Lão trừng mắt nhìn ta, sát khí đằng đằng.

Ta mỉm cười, chắp tay thi lễ một cách nho nhã: "Vạn Độc Môn, Lệ Vô Tâm. Nghe danh Lý Gia đã lâu, nay đặc biệt đến... tiễn đưa."

"Vạn Độc Môn?!"

Sắc mặt Lý Thiên Bá biến đổi. Cái tên này ở Nam Cương đồng nghĩa với tai ương. Nhưng ỷ vào số đông và tu vi cao hơn, lão vẫn cứng giọng: "Tiểu tử cuồng vọng! Một mình ngươi dám chống lại cả Lý Gia ta sao? Giết hắn!"

Cả đám tu sĩ lao lên, pháp bảo bay rợp trời. Kiếm khí, đao quang, hỏa cầu... tất cả nhắm thẳng vào ta.

Ta không hề nao núng. Ta mở Huyết Độc Phiến, vận chuyển [Vạn Độc Phệ Hồn Quyết](../../Công_Pháp/Vạn_Độc_Phệ_Hồn_Quyết.md).

"Vạn Độc... Phệ Tâm!"

Từ chiếc quạt, hàng ngàn con Cổ trùng vô hình bay ra, lách qua khe hở của pháp bảo, chui tọt vào cơ thể đối phương.

*Á á á!*

Tiếng kêu la thảm thiết vang lên liên hồi. Những kẻ trúng chiêu ôm ngực lăn lộn dưới đất, mặt mày tím tái, thất khiếu chảy máu. Tim bọn chúng đang bị Cổ trùng gặm nhấm từng chút một.

Lý Thiên Bá kinh hoàng nhìn cảnh tượng trước mắt. Đám con cháu, đệ tử tinh anh của lão ngã rạ như ngả rạ chỉ sau một chiêu.

"Ngươi... ngươi là quỷ dữ!"

Lão gầm lên, tế ra một thanh phi kiếm thượng phẩm, định liều chết với ta.

Nhưng ta đã nhanh hơn.

*Vút!*

Một bóng đỏ lướt qua. Con [Thiên Tinh Cổ](../../Kỳ_Vật/Thiên_Tinh_Cổ.md) bản mệnh của ta đã cắn phập vào cổ lão.

"Ư..."

Lý Thiên Bá cứng đờ người, thanh kiếm rơi xuống đất *keng* một tiếng. Độc tố lan nhanh, biến lão thành một bức tượng máu sống động.

Ta bước tới gần, nhìn vào đôi mắt đang dần mất đi sự sống của lão.

"Kiếp sau nhớ kỹ," ta thì thầm vào tai lão. "Đừng bao giờ động vào đồ của Vạn Độc Môn."

Đêm hôm đó, Lý Gia diệt môn. Máu chảy thành sông, nhuộm đỏ cả sân gạch trắng. Ta đứng giữa biển xác chết, phe phẩy chiếc quạt xương, cảm thấy lòng bình thản đến lạ lùng.

Từ nay về sau, cái tên [Huyết Thủ Thư Sinh] sẽ vang danh khắp Nam Cương. Và không kẻ nào dám coi thường Lệ Vô Tâm ta nữa.
