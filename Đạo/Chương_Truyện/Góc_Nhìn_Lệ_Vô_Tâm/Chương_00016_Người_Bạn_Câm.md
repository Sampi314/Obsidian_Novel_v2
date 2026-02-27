<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00015_Ánh_Mắt_Của_Sư_Phụ.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a id="next-chapter-link" href="Chương_00017_Những_Bữa_Ăn_Vụng_Trộm.html">Chương Sau ➡️</a></td>
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
<li style="padding: 5px; "><a href="Chương_00008_Diện_Kiến_Lão_Quái.html">Chương 8: Diện Kiến Lão Quái</a></li>
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00016_Người_Bạn_Câm.html">Chương 16: Người Bạn Câm</a></li>
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
    var nextChapterUrl = "Chương_00017_Những_Bữa_Ăn_Vụng_Trộm.html";

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
# Chương 16: Người Bạn Câm

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Lệ Vô Tâm](../../Nhân_Vật/Lệ_Vô_Tâm.md)
**Địa điểm:** Vạn Độc Môn (Dược Điền).
**Thời điểm:** 2 năm sau Huyết Trì (Hữu Tâm 15 tuổi).
**Giao Điểm Cốt Truyện:** Tuyến độc lập (Quá khứ).

---

Hai năm đã trôi qua. Ta mười lăm tuổi, nhưng nhìn vào gương nước, ta thấy một gương mặt già nua của một kẻ đã sống cả trăm năm. Da ta trắng bệch như sáp nến, đôi mắt sâu hoắm, và trên cơ thể không còn một tấc da thịt nào nguyên vẹn.

Ta được phép ra ngoài. Độc Cô Lão Quái giao cho ta nhiệm vụ chăm sóc khu Dược Điền phía tây, nơi trồng những cây Huyết Mộc non. Công việc này không nặng nhọc, nhưng đòi hỏi sự tỉ mỉ. Nếu để chết một cây, ta sẽ bị phạt ngâm mình trong bể axit ba ngày.

Ta đang lúi húi xới đất, chợt nghe tiếng sột soạt sau lưng.

Ta quay phắt lại, tay đã thủ sẵn một con dao găm tẩm độc.

Một bóng người nhỏ bé đang co rúm lại sau gốc cây Huyết Mộc. Đó là một tên tạp dịch, mặc bộ quần áo rách nát, mặt mày lấm lem bùn đất. Hắn nhìn ta với đôi mắt to tròn, sợ hãi.

"Ai?" Ta gằn giọng.

Hắn không trả lời, chỉ lắc đầu lia lịa, tay chân run rẩy. Hắn chỉ vào cái giỏ mây bên cạnh, rồi lại chỉ vào miệng mình, ra hiệu xin ăn.

Ta cau mày. "Ngươi bị câm?"

Hắn gật đầu.

Ta nhìn hắn một lúc lâu. Hắn gầy gò, yếu ớt, chẳng khác gì con chó hoang mà ta đã giết hai năm trước. Trong Vạn Độc Môn này, những kẻ như hắn thường không sống quá ba tháng. Vậy mà hắn vẫn sống, vẫn đi xin ăn.

Ta hạ con dao xuống. Một cảm giác kỳ lạ dâng lên trong lòng. Có lẽ vì hắn giống ta của ngày xưa. Có lẽ vì đôi mắt hắn không chứa đựng sự toan tính hay thù hận, chỉ đơn thuần là bản năng sinh tồn.

"Biến đi," ta nói, nhưng tay lại ném cho hắn nửa cái bánh bao khô khốc mà ta mang theo.

Hắn chộp lấy cái bánh như vớ được vàng, cúi đầu cảm tạ rối rít rồi chạy biến vào rừng.

Ngày hôm sau, hắn lại đến. Lần này hắn mang theo một nắm quả dại màu đỏ mọng. Hắn rụt rè đặt xuống trước mặt ta, rồi lùi lại vài bước, chờ đợi.

Ta nhìn nắm quả dại. Đây là Huyết Long Quả, một loại quả có độc tính nhẹ, nhưng lại rất tốt cho việc bồi bổ khí huyết. Hắn tìm đâu ra thứ này?

"Ngươi... cho ta?" Ta hỏi.

Hắn gật đầu, mỉm cười. Nụ cười ngây ngô, để lộ hàm răng sún.

Ta cầm một quả lên, cắn thử. Vị chua ngọt lan tỏa trong miệng, làm dịu đi vị đắng ngắt của thuốc độc mà ta phải uống hàng ngày.

"Tên ngươi là gì?"

Hắn lấy một cành cây khô, viết lên mặt đất chữ "Mộc" nghuệch ngoạc.

"A Mộc?"

Hắn gật đầu lia lịa, ánh mắt sáng lên.

Từ hôm đó, A Mộc trở thành cái bóng của ta. Hắn giúp ta xới đất, tưới nước cho cây Huyết Mộc. Hắn không nói được, nhưng hắn rất thạo việc. Những lúc rảnh rỗi, hắn thường ngồi bên cạnh ta, nghe ta kể lảm nhảm về những thứ vô nghĩa mà ta nhìn thấy trong sách độc dược.

Hắn là người duy nhất không sợ ta. Hắn là người duy nhất nhìn ta như một con người, chứ không phải một con quái vật.

Ta bắt đầu dạy hắn một vài chiêu thức phòng thân cơ bản. Ta chia sẻ cho hắn những khẩu phần ăn ít ỏi của mình. Ta thậm chí còn lén lấy thuốc trị thương của Lão Quái để bôi lên những vết roi trên lưng hắn.

Dần dần, ta cảm thấy mình đang sống lại. Trái tim băng giá của ta bắt đầu tan chảy. Ta tự nhủ, có lẽ trong cái địa ngục trần gian này, vẫn còn tồn tại một chút gì đó gọi là tình người.

A Mộc... ta sẽ bảo vệ ngươi. Dù có phải chống lại cả Vạn Độc Môn này, ta cũng sẽ không để ai làm hại ngươi.

Nhưng lúc đó, ta đâu biết rằng, chính sự tin tưởng ngây thơ ấy lại là nhát dao chí mạng, đẩy ta xuống vực thẳm tăm tối hơn cả cái chết.
