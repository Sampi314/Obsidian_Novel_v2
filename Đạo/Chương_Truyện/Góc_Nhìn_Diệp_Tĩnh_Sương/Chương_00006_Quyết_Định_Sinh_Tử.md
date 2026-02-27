---
Tác_Giả: Jules (Tổng Quản)
Ngày_Viết: 2026-03-08
Góc_Nhìn: Diệp Tĩnh Sương
Bối_Cảnh: Pháo Đài Xanh
Nhân_Vật: Diệp Tĩnh Sương, Lâm Phong, Hứa Thanh Vân
Ghi_Chú: Khoảnh khắc bình yên ngắn ngủi trước khi rời Pháo Đài Xanh.
---
<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00005_Thoát_Khỏi_Địa_Ngục.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px; color: #adb5bd;">Chương Sau ➡️</td>
</tr>
</table>
<details style="margin-top: 10px;">
<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>
<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">
<li style="padding: 5px; "><a href="Chương_00000_Tuyết_Phủ_Mộ_Phần.html">Chương 0: Tuyết Phủ Mộ Phần</a></li>
<li style="padding: 5px; "><a href="Chương_00000_5_Thử_Thách_Đầu_Tiên.html">Chương 0.5: Thử Thách Đầu Tiên</a></li>
<li style="padding: 5px; "><a href="Chương_00001_Nhiệm_Vụ_Đơn_Độc.html">Chương 1: Nhiệm Vụ Đơn Độc</a></li>
<li style="padding: 5px; "><a href="Chương_00001_5_Dấu_Vết_Tàn_Khốc.html">Chương 1.5: Dấu Vết Tàn Khốc</a></li>
<li style="padding: 5px; "><a href="Chương_00002_Hội_Ngộ_Bất_Ngờ.html">Chương 2: Hội Ngộ Bất Ngờ</a></li>
<li style="padding: 5px; "><a href="Chương_00003_Lời_Thề_Kiếm_Khách.html">Chương 3: Lời Thề Kiếm Khách</a></li>
<li style="padding: 5px; "><a href="Chương_00004_Lạc_Giữa_Thâm_Cung.html">Chương 4: Lạc Giữa Thâm Cung</a></li>
<li style="padding: 5px; "><a href="Chương_00005_Thoát_Khỏi_Địa_Ngục.html">Chương 5: Thoát Khỏi Địa Ngục</a></li>
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00006_Quyết_Định_Sinh_Tử.html">Chương 6: Quyết Định Sinh Tử</a></li>
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
    var nextChapterUrl = "#";

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
# Chương 6: Quyết Định Sinh Tử

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Diệp Tĩnh Sương](../../Nhân_Vật/Diệp_Tĩnh_Sương.md)
**Nhân vật liên quan:** [Lâm Phong](../../Nhân_Vật/Lâm_Phong.md), [Hứa Thanh Vân](../../Nhân_Vật/Hứa_Thanh_Vân.md)
**Địa điểm:** [Pháo Đài Xanh](../../Kỳ_Vật/Xương_Rồng_Thiên_Trụ.md).
**Thời điểm:** Giữa [Chương 34: Pháo Đài Xanh](../Góc_Nhìn_Chính/Chương_00034_Pháo_Đài_Xanh.md) và [Chương 35: Lối Mòn Trong Bão](../Góc_Nhìn_Chính/Chương_00035_Lối_Mòn_Trong_Bão.md).
**Giao Điểm Cốt Truyện:** Diệp Tĩnh Sương quyết định rời khỏi nơi trú ẩn an toàn để tiến vào Rừng Huyết Độc.

---

Ánh trăng trong vắt soi bóng xuống mặt hồ yên ả của *Pháo Đài Xanh*. Không gian tĩnh lặng đến mức ta có thể nghe thấy tiếng dế kêu râm ran trong bụi cỏ - một âm thanh xa xỉ giữa vùng đất chết Tây Mạc này.

Ta ngồi trên bệ đá cổ xưa giữa hồ, để chân trần ngâm trong làn nước mát lạnh. *Hàn Ngọc Kiếm* nằm im lìm bên cạnh, phản chiếu ánh sáng bàng bạc. Lần đầu tiên sau nhiều ngày, ta mới có thể thả lỏng cơ thể, trút bỏ lớp áo giáp phòng bị thường trực.

Nhưng trong lòng ta, sóng gió vẫn chưa bao giờ dứt.

Hình ảnh Lục Ly tan biến vào hư không vẫn ám ảnh tâm trí ta. Ánh mắt kiên định của nàng, nụ cười thanh thản khi chấp nhận hy sinh... tất cả như một tảng đá nặng đè lên ngực ta. Nàng đã trao cho ta cơ hội sống, và cả gánh nặng của trách nhiệm cứu vãn vùng đất này.

"Tỷ đang nghĩ gì vậy?"

Một giọng nói trầm ấm vang lên, phá tan dòng suy tưởng của ta. Lâm Phong bước tới, tay cầm hai quả *Xương Rồng Đỏ* chín mọng vừa hái được.

"Về con đường phía trước," ta đáp, không quay đầu lại.

Lâm Phong ngồi xuống cạnh ta, đưa một quả cho ta. "Ăn chút đi. Ngọt lắm."

Ta cầm lấy quả, nhưng không ăn ngay. Ta nhìn vào mặt hồ, nơi phản chiếu khuôn mặt mệt mỏi của chính mình.

"Lâm Phong, đệ có sợ không?"

"Sợ chứ," hắn cười, nụ cười chân thật và có chút ngây ngô của một thiếu niên mười sáu tuổi. "Ta sợ chết. Sợ không bao giờ được gặp lại mẹ. Sợ... không bảo vệ được mọi người."

Hắn dừng lại một chút, rồi nhìn thẳng vào mắt ta. "Nhưng ta còn sợ hơn nếu phải sống chui lủi ở đây cả đời, trong khi biết rằng thế giới ngoài kia đang sụp đổ vì sai lầm của chúng ta."

Ta sững người. Sai lầm của chúng ta. Hắn không đổ lỗi cho ai, mà tự nhận lấy phần trách nhiệm về mình. Chàng trai trẻ này đã trưởng thành hơn ta tưởng rất nhiều.

"Ta cũng vậy," ta khẽ nói. "Pháo Đài Xanh là một nơi tuyệt vời. An toàn, đầy đủ lương thực, nước uống. Chúng ta có thể sống ở đây mười năm, hai mươi năm, thậm chí đến già. Nhưng..."

"Nhưng đó không phải là cách sống của Diệp Tĩnh Sương," Lâm Phong tiếp lời, giọng chắc nịch. "Và cũng không phải là cách sống của Lâm Phong."

Ta mỉm cười. Hắn hiểu ta.

"Ngày mai chúng ta sẽ lên đường," ta tuyên bố, giọng trở nên kiên quyết. "Mục tiêu là Nam Cương. Rừng Huyết Độc."

"Ta đã xem bản đồ," Lâm Phong nhíu mày. "Đường đến đó phải đi qua *Ranh Giới Tử Thần*. Nghe đồn ở đó có những sinh vật biến dị cực kỳ nguy hiểm, chưa kể đến tai mắt của Vạn Độc Môn."

"Ta biết," ta gật đầu. "Lệ Vô Tâm chắc chắn đã đoán được đường đi của chúng ta. Hắn là kẻ thông minh và xảo quyệt. Hắn sẽ không để yên cho chúng ta đến Nam Cương dễ dàng đâu."

"Vậy tỷ định đối phó thế nào?"

Ta nắm chặt chuôi kiếm *Hàn Ngọc*. Hơi lạnh từ thanh kiếm truyền sang tay ta, giúp ta tỉnh táo hơn bao giờ hết.

"Chúng ta không thể trốn chạy mãi được. Đã đến lúc phải chủ động tấn công. Hắn muốn giăng bẫy, ta sẽ phá bẫy. Hắn muốn chơi trò mèo vờn chuột, ta sẽ cho hắn thấy con chuột này có nanh vuốt sắc bén thế nào."

Ta quay sang nhìn Lâm Phong. "Đệ hãy chuẩn bị tên lửa và thuốc nổ. Chúng ta sẽ cần đến chúng."

"Đã rõ!" Lâm Phong đứng phắt dậy, vẻ mặt hừng hực khí thế. "Ta đi bảo Hứa Thanh Vân chuẩn bị lương khô ngay."

Bóng dáng Lâm Phong khuất dần sau những tán cây xương rồng khổng lồ. Ta ở lại một mình, tiếp tục ngắm trăng.

Ngày mai, khi mặt trời mọc, sự bình yên này sẽ kết thúc. Chúng ta sẽ bước vào hang ổ của quỷ dữ. Có thể ta sẽ không bao giờ trở lại, nhưng ta không hối tiếc.

Vì ta là Diệp Tĩnh Sương. Ta sống vì kiếm, và sẽ chết vì kiếm.

Ta đứng dậy, tra kiếm vào vỏ. Một luồng kiếm khí sắc bén bùng lên quanh người, xua tan đi màn đêm tĩnh mịch.

*Nam Cương, hãy đợi đấy.*
