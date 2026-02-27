<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00001_5_Dấu_Vết_Tàn_Khốc.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a id="next-chapter-link" href="Chương_00003_Lời_Thề_Kiếm_Khách.html">Chương Sau ➡️</a></td>
</tr>
</table>
<details style="margin-top: 10px;">
<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>
<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">
<li style="padding: 5px; "><a href="Chương_00000_Tuyết_Phủ_Mộ_Phần.html">Chương 0: Tuyết Phủ Mộ Phần</a></li>
<li style="padding: 5px; "><a href="Chương_00000_5_Thử_Thách_Đầu_Tiên.html">Chương 0.5: Thử Thách Đầu Tiên</a></li>
<li style="padding: 5px; "><a href="Chương_00001_Nhiệm_Vụ_Đơn_Độc.html">Chương 1: Nhiệm Vụ Đơn Độc</a></li>
<li style="padding: 5px; "><a href="Chương_00001_5_Dấu_Vết_Tàn_Khốc.html">Chương 1.5: Dấu Vết Tàn Khốc</a></li>
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00002_Hội_Ngộ_Bất_Ngờ.html">Chương 2: Hội Ngộ Bất Ngờ</a></li>
<li style="padding: 5px; "><a href="Chương_00003_Lời_Thề_Kiếm_Khách.html">Chương 3: Lời Thề Kiếm Khách</a></li>
<li style="padding: 5px; "><a href="Chương_00004_Lạc_Giữa_Thâm_Cung.html">Chương 4: Lạc Giữa Thâm Cung</a></li>
<li style="padding: 5px; "><a href="Chương_00005_Thoát_Khỏi_Địa_Ngục.html">Chương 5: Thoát Khỏi Địa Ngục</a></li>
<li style="padding: 5px; "><a href="Chương_00006_Quyết_Định_Sinh_Tử.html">Chương 6: Quyết Định Sinh Tử</a></li>
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
    var nextChapterUrl = "Chương_00003_Lời_Thề_Kiếm_Khách.html";

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
# Chương 2: Hội Ngộ Bất Ngờ

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Diệp Tĩnh Sương](../../Nhân_Vật/Diệp_Tĩnh_Sương.md)
**Nhân vật liên quan:** [Lâm Phong](../../Nhân_Vật/Lâm_Phong.md)
**Địa điểm:** Thôn Lạc Diệp.
**Thời điểm:** Song song với [Chương 2: Huyết Tướng](../Góc_Nhìn_Chính/Chương_00002_Huyết_Tướng.md).
**Giao Điểm Cốt Truyện:** Lần đầu gặp gỡ Lâm Phong.

---

Cơn mưa bắt đầu nặng hạt, rửa trôi đi lớp bụi trần nhưng không thể xóa nhòa mùi máu tanh nồng nặc đang bao trùm lấy Thôn Lạc Diệp.

Ta bước đi giữa những xác người nằm la liệt. Có người già, có trẻ nhỏ, tất cả đều chết trong tư thế đau đớn tột cùng. Da thịt họ tím tái, mạch máu đen sì nổi lên như rễ cây cổ thụ – dấu hiệu đặc trưng của [Huyết Thần Độc](../../Kỳ_Vật/Huyết_Thần_Độc.md).

"Vạn Độc Môn..." Ta nghiến răng, tay siết chặt chuôi kiếm đến mức khớp xương trắng bệch.

Bọn chúng không tha cho bất cứ ai. Sự tàn độc này khiến ta nhớ lại đêm định mệnh năm xưa. Cổ họng ta nghẹn đắng, một cảm giác buồn nôn dâng lên nhưng nhanh chóng bị ta dùng chân khí đè nén xuống.

Bỗng nhiên, tai ta bắt được một tiếng động lạ.

*Két...*

Tiếng cửa gỗ cọt kẹt phát ra từ một ngôi nhà tranh ở cuối thôn. Có người còn sống? Hay là kẻ thù vẫn còn lảng vảng?

Ta nín thở, thi triển bộ pháp nhẹ nhàng áp sát ngôi nhà. [Hàn Mai Kiếm](../../Luyện_Khí/Hàn_Ngọc_Kiếm.md) rời vỏ một tấc, hàn khí tỏa ra lạnh buốt.

*Xoạt!*

Ta tung cửa xông vào, mũi kiếm chỉ thẳng vào bóng người đang đứng giữa nhà.

"Ai?!"

Người đó giật mình quay lại. Là một nam tử trẻ tuổi, vận y phục vải thô của tán tu. Trên tay hắn đang cầm một mảnh ngọc bội vỡ nát nhặt được từ dưới đất.

Hắn nhìn ta, đôi mắt đen láy thoáng chút ngạc nhiên nhưng không hề sợ hãi.

"Cô nương bình tĩnh, ta không phải kẻ thù," hắn nói, giọng điệu trầm ổn đến lạ lùng so với hoàn cảnh hiện tại.

Ta nheo mắt đánh giá hắn. Luyện Khí tầng chín... không, Luyện Khí Viên Mãn. Khí tức bình thường, không có sát khí, cũng không có tà khí. Chỉ là một tán tu vô danh tiểu tốt. Nhưng tại sao hắn lại ở đây? Và tại sao khi đối diện với kiếm ý của ta – một đệ tử chân truyền Cửu Hoa Kiếm Tông – hắn lại có thể bình thản đến thế?

"Ngươi là ai? Tại sao lại ở nơi này?" Ta lạnh lùng hỏi, kiếm vẫn không hạ xuống.

"Tại hạ là Lâm Phong, một tán tu đi ngang qua đây," hắn đáp, nhẹ nhàng đặt mảnh ngọc bội xuống bàn. "Ta thấy ngôi làng có dấu hiệu bất thường nên vào kiểm tra, không ngờ..." Hắn thở dài, nhìn quanh căn nhà hoang tàn. "Thảm quá."

Ánh mắt hắn dừng lại trên thi thể một đứa bé nằm trong góc nhà. Ta thấy cơ mặt hắn khẽ giật, một tia đau xót chân thật hiện lên trong đáy mắt.

Sát ý trong ta dịu xuống đôi chút. Kẻ này... có lẽ không nói dối. Nhưng ta vẫn không thể lơ là cảnh giác. Giang hồ hiểm ác, kẻ mang bộ mặt thiện lương chưa chắc đã là người tốt.

"Rời khỏi đây đi," ta thu kiếm về, giọng nói vẫn lạnh băng như sương giá. "Nơi này không phải chỗ cho ngươi dạo chơi. Kẻ gây ra chuyện này không đơn giản đâu."

Lâm Phong nhìn ta, rồi nhìn thanh kiếm bên hông ta.

"Hàn khí bức người, kiếm pháp sắc bén... Cô nương chắc là đệ tử của Cửu Hoa Kiếm Tông?" Hắn hỏi ngược lại.

Ta không đáp, quay người định bỏ đi. Ta không có thói quen dây dưa với người lạ, nhất là trong lúc làm nhiệm vụ.

"Khoan đã," hắn gọi với theo. "Cô nương định đi tìm lũ hung thủ sao? Ta vừa phát hiện ra một dấu vết lạ ở giếng nước phía sau thôn."

Bước chân ta khựng lại. Giếng nước?

"Dẫn đường," ta nói ngắn gọn.

Lâm Phong gật đầu, bước ra trước dẫn đường. Nhìn bóng lưng hắn, ta thầm đánh giá lại. Tuy tu vi không cao, nhưng khả năng quan sát của hắn có vẻ không tồi. Và quan trọng hơn, hắn dám ở lại nơi tử địa này để điều tra, chứng tỏ tâm tính cũng không phải hạng tham sống sợ chết.

Chúng ta đi đến bên giếng nước cổ. Mùi tanh hôi ở đây nồng nặc hơn hẳn những chỗ khác. Ta cúi xuống nhìn, đáy giếng tối om như hũ nút, nhưng ta có thể cảm nhận được một luồng oán khí đang cuộn trào bên dưới.

"Cẩn thận," Lâm Phong bỗng lên tiếng cảnh báo, tay hắn đã đặt lên cây cung gỗ đeo sau lưng.

Cùng lúc đó, mặt đất dưới chân ta rung chuyển dữ dội.

*Rầm!*

Đất đá bắn tung tóe. Một bóng đen khổng lồ lao vút lên từ lòng giếng, mang theo mùi máu tanh lợm giọng.

[Huyết Tướng](../../Kỳ_Vật/Huyết_Tướng.md)!

Ta lập tức rút kiếm, thân hình lùi lại phía sau, tạo thế thủ.

"Quái vật gì thế này?" Lâm Phong thốt lên, nhưng tay hắn đã nhanh chóng kéo căng dây cung. Ba mũi tên lửa xuất hiện trên tay hắn.

Ta liếc nhìn hắn một cái. *Hỏa hệ thuật pháp?* Cũng có chút bản lĩnh.

"Đừng để nó chạm vào người! Máu nó có độc!" Ta hét lên, rồi lao vào con quái vật.

Khoảnh khắc đó, ta không ngờ rằng, cuộc gặp gỡ tình cờ giữa cơn mưa máu này sẽ mở đầu cho một hành trình dài đầy gian nan, và kẻ tán tu có cái tên Lâm Phong kia, sẽ trở thành người duy nhất có thể làm tan chảy lớp băng trong lòng ta.

Nhưng đó là chuyện của sau này. Còn bây giờ...

*Chết đi!*

Hàn Mai Kiếm trong tay ta lóe lên, vạch một đường kiếm quang rực rỡ xé toạc màn đêm.
