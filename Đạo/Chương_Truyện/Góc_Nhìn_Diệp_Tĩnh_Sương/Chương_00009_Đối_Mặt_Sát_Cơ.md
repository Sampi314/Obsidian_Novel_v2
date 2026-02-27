---
Tác_Giả: Jules (Tổng Quản)
Ngày_Viết: 2026-03-08
Góc_Nhìn: Diệp Tĩnh Sương
Bối_Cảnh: Hành Trình Rời Pháo Đài Xanh - Ranh Giới Tử Thần
Nhân_Vật: Diệp Tĩnh Sương, Lâm Phong
Ghi_Chú: Suy nghĩ nội tâm của Diệp Tĩnh Sương trên đường tiến vào Rừng Huyết Độc.
---
<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00008_Lời_Thề_Kiếm_Khách.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a id="next-chapter-link" href="Chương_00010_Lạc_Giữa_Thâm_Cung.html">Chương Sau ➡️</a></td>
</tr>
</table>
<details style="margin-top: 10px;">
<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>
<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">
<li style="padding: 5px; "><a href="Chương_00001_Tuyết_Phủ_Mộ_Phần.html">Chương 1: Tuyết Phủ Mộ Phần</a></li>
<li style="padding: 5px; "><a href="Chương_00002_Dấu_Vết_Tàn_Khốc.html">Chương 2: Dấu Vết Tàn Khốc</a></li>
<li style="padding: 5px; "><a href="Chương_00003_Thử_Thách_Đầu_Tiên.html">Chương 3: Thử Thách Đầu Tiên</a></li>
<li style="padding: 5px; "><a href="Chương_00004_Nhiệm_Vụ_Đơn_Độc.html">Chương 4: Nhiệm Vụ Đơn Độc</a></li>
<li style="padding: 5px; "><a href="Chương_00006_Hội_Ngộ_Bất_Ngờ.html">Chương 6: Hội Ngộ Bất Ngờ</a></li>
<li style="padding: 5px; "><a href="Chương_00007_Quyết_Định_Sinh_Tử.html">Chương 7: Quyết Định Sinh Tử</a></li>
<li style="padding: 5px; "><a href="Chương_00008_Lời_Thề_Kiếm_Khách.html">Chương 8: Lời Thề Kiếm Khách</a></li>
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00009_Đối_Mặt_Sát_Cơ.html">Chương 9: Đối Mặt Sát Cơ</a></li>
<li style="padding: 5px; "><a href="Chương_00010_Lạc_Giữa_Thâm_Cung.html">Chương 10: Lạc Giữa Thâm Cung</a></li>
<li style="padding: 5px; "><a href="Chương_00011_Thoát_Khỏi_Địa_Ngục.html">Chương 11: Thoát Khỏi Địa Ngục</a></li>
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
    var nextChapterUrl = "Chương_00010_Lạc_Giữa_Thâm_Cung.html";

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
# Chương 9: Đối Mặt Sát Cơ

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Diệp Tĩnh Sương](../../Nhân_Vật/Diệp_Tĩnh_Sương.md)
**Nhân vật liên quan:** [Lâm Phong](../../Nhân_Vật/Lâm_Phong.md)
**Địa điểm:** [Ranh Giới Tử Thần](../../Thế_Giới_Và_Thời_Gian/Vùng_Đất_Chết.md).
**Thời điểm:** Song song với [Chương 36](../Góc_Nhìn_Chính/Chương_00036_Ranh_Giới_Tử_Thần.md) và [Chương 37](../Góc_Nhìn_Chính/Chương_00037_Vòng_Vây_Huyết_Lang.md).
**Giao Điểm Cốt Truyện:** Diệp Tĩnh Sương cảm nhận được mối nguy hiểm đang chờ đợi và chuẩn bị tinh thần chiến đấu.

---

Rời khỏi Pháo Đài Xanh, ta như bước từ thiên đường xuống địa ngục trần gian.

Mùi không khí trong lành, mát mẻ của ốc đảo nhanh chóng bị thay thế bởi hơi nóng hầm hập và mùi khét lẹt của cát cháy. Gió rít gào bên tai, mang theo những hạt cát sắc nhọn quất vào mặt, vào da thịt đau rát. Nhưng điều đó không đáng sợ bằng cảm giác ớn lạnh chạy dọc sống lưng ta.

Sát khí.

Nó lẩn khuất đâu đó trong màn sương mù màu tím đang cuộn trào phía trước. Không phải sát khí của thiên nhiên khắc nghiệt, mà là sát khí của con người, của dã thú được huấn luyện để giết chóc.

"Tĩnh Sương tỷ, tỷ thấy sao?" Lâm Phong đi bên cạnh ta, tay lăm lăm cây cung, giọng nói có chút run rẩy nhưng ánh mắt vẫn kiên định.

"Cẩn thận," ta đáp gọn lỏn, mắt không rời khỏi những bóng cây *Huyết Mộc* vặn vẹo phía xa. "Chúng ta đang bị theo dõi."

Ta cảm nhận được những ánh mắt đó. Hàng trăm ánh mắt hau háu, tham lam, đang dõi theo từng bước chân của chúng ta. Chúng ẩn mình trong bóng tối, trong những bụi cây rậm rạp, kiên nhẫn chờ đợi thời cơ để lao ra xé xác con mồi.

Ta siết chặt chuôi kiếm *Hàn Ngọc*. Hơi lạnh từ thanh kiếm truyền sang tay ta, giúp ta bình tĩnh lại. Ta nhớ đến lời dạy của sư phụ: *"Kiếm giả, tâm phải tĩnh như nước. Dù trước mặt là núi đao biển lửa, tâm không loạn thì kiếm mới sắc."*

Nhưng làm sao có thể tĩnh tâm được khi phía sau lưng ta là hai mẹ con Hứa gia yếu đuối? Hứa Nhược Thủy đang thoi thóp vì độc tố, còn Hứa Thanh Vân thì chỉ là một thiếu niên chưa trải sự đời. Ta không chỉ chiến đấu cho bản thân mình, mà còn gánh trên vai mạng sống của họ.

*Vút!*

Một mũi tên của Lâm Phong xé gió lao đi, găm thẳng vào bụi cây phía trước. Tiếng rên rỉ của một con sói vang lên, rồi im bặt.

"Bắt đầu rồi," ta thầm nghĩ.

Tiếng hú ghê rợn vang lên tứ phía. Những bóng đen lao ra từ màn sương, nhe nanh múa vuốt. Là *Huyết Độc Lang*. Ta nhận ra chúng ngay lập tức. Loài sói biến dị này ta từng nghe sư phụ nhắc đến, chúng là "chó săn" của Vạn Độc Môn.

"Bảo vệ Hứa phu nhân!" Ta hét lớn, *Hàn Ngọc Kiếm* tuốt khỏi vỏ.

Đường kiếm của ta vẽ nên những vòng tròn ánh sáng xanh lam, tạo thành một kết giới băng giá. Mỗi nhát chém là một con sói ngã xuống, máu đen chảy ra đông cứng lại. Nhưng chúng quá đông, và quá điên cuồng.

Trong lúc giao chiến, ta nghe thấy tiếng sáo.

Âm thanh đó như ma chú, len lỏi vào tâm trí, kích động sự hung hãn của bầy sói. Ta biết kẻ thổi sáo là ai. Chỉ có thể là hắn - Lệ Vô Tâm.

Hắn đang ở đâu đó ngoài kia, quan sát chúng ta như một kẻ thợ săn đang vờn con mồi. Hắn muốn thấy sự sợ hãi, sự tuyệt vọng của chúng ta.

Nhưng hắn đã lầm.

Ta là Diệp Tĩnh Sương, đệ tử chân truyền của Kiếm Tông. Ta có thể chết, nhưng tuyệt đối không bao giờ cúi đầu trước cái ác.

"Lâm Phong, dùng Hỏa Linh Tiễn!" Ta ra lệnh, quyết đoán và lạnh lùng.

Ngọn lửa bùng lên, thiêu đốt lũ sói và mở ra một con đường máu. Nhưng con đường đó không dẫn về phía sa mạc, mà dẫn sâu hơn vào *Rừng Huyết Độc*.

Ta biết đó là cái bẫy. Lệ Vô Tâm đang lùa chúng ta vào đó. Nhưng ta cũng biết, đó là cơ hội duy nhất.

"Vùng Đất Chết..." Ta lẩm bẩm cái tên đáng sợ ấy khi nhìn thấy vòm cổng *Huyết Mộc* chết khô phía trước.

Nơi đó là tử địa, nhưng cũng có thể là sinh cơ. Nếu chúng ta vượt qua được, chúng ta sẽ sống. Còn nếu không...

Ta nhìn sang Lâm Phong, thấy cậu thiếu niên gật đầu đầy quyết tâm. Ta nhìn Hứa Thanh Vân đang run rẩy nhưng vẫn nắm chặt thanh kiếm cùn.

"Đi thôi," ta nói, giọng chắc nịch. "Vào hang cọp để bắt cọp con."

Chúng ta lao vào bóng tối, bỏ lại sau lưng tiếng cười man dại của Lệ Vô Tâm và bầy sói đói khát. Cuộc chiến thực sự mới chỉ bắt đầu.
