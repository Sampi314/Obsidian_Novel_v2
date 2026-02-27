<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00006_Truy_Vết_Tử_Thần.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a id="next-chapter-link" href="Chương_00008_Huyết_Tế_Sa_Mạc.html">Chương Sau ➡️</a></td>
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
<li style="padding: 5px; "><a href="Chương_00006_Truy_Vết_Tử_Thần.html">Chương 6: Truy Vết Tử Thần</a></li>
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00007_Dưới_Bóng_Hắc_Sa.html">Chương 7: Dưới Bóng Hắc Sa</a></li>
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
    var nextChapterUrl = "Chương_00008_Huyết_Tế_Sa_Mạc.html";

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
# Chương 7: Dưới Bóng Hắc Sa

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Lệ Vô Tâm](../../Nhân_Vật/Lệ_Vô_Tâm.md)
**Nhân vật liên quan:** [Huyết Vệ](../../Nhân_Vật/Huyết_Vệ.md)
**Địa điểm:** Rìa Rừng Huyết Độc - Giáp ranh Tây Mạc.
**Thời điểm:** Song song với sự kiện [Long Cốt](../../Kỳ_Vật/Long_Cốt.md) bị phá vỡ (Chương 30).
**Giao Điểm Cốt Truyện:** [Chương 31: Hắc Sa Bão Trỗi Dậy](../Góc_Nhìn_Chính/Chương_00031_Hắc_Sa_Bão_Trỗi_Dậy.md).

---

Mặt đất dưới chân ta rung chuyển dữ dội, không phải là cơn chấn động nhẹ nhàng như khi [Huyết Tướng](../../Kỳ_Vật/Huyết_Tướng.md) xuất hiện, mà là một sự rung lắc tận sâu trong lòng đất, như thể chính thế giới này đang rên rỉ vì đau đớn.

"Thánh Tử! Nhìn kìa!"

Tiếng hét kinh hoàng của một tên Huyết Vệ kéo ta ra khỏi dòng suy nghĩ. Ta ngẩng đầu lên, nhìn về phía chân trời Tây Mạc.

Và ta thấy nó.

Một cột sáng khổng lồ màu vàng đất bắn thẳng lên trời cao, xé toạc màn đêm tĩnh mịch. Nhưng chỉ trong chớp mắt, cột sáng ấy bị nhuộm đen bởi một thứ bóng tối đặc quánh, cuồn cuộn như mực loang trong nước.

*Ầm!*

Tiếng nổ vang lên sau đó, chậm hơn ánh sáng nhưng sức công phá thì khủng khiếp hơn gấp bội. Sóng xung kích quét qua sa mạc, cuốn theo cát bụi tạo thành một bức tường khổng lồ đang lao về phía chúng ta với tốc độ chóng mặt.

"Là... [Long Cốt](../../Kỳ_Vật/Long_Cốt.md)..." Ta thì thầm, đôi mắt mở to hết cỡ. "Phong ấn đã bị phá vỡ."

Lâm Phong... Diệp Tĩnh Sương... Các ngươi đã làm cái quái gì thế này?

Ta cứ ngỡ chúng chỉ lẻn vào trộm một chút bảo vật, hay cùng lắm là tìm đường sống trong chỗ chết. Nhưng không, chúng đã phá hủy long mạch! Chúng đã đánh thức thứ mà ngay cả các trưởng lão Vạn Độc Môn cũng phải kiêng dè: [Địa Sát](../../Kỳ_Vật/Địa_Sát.md).

"Thánh Tử! Bão cát đang tới! Chúng ta phải rút lui thôi!" Tên thủ lĩnh Huyết Vệ hoảng loạn thúc giục.

Ta liếc nhìn hắn. Sự sợ hãi hiện rõ trên khuôn mặt vốn đã quen với chết chóc. Cũng phải thôi, [Hắc Sa Bão](../../Kỳ_Vật/Hắc_Sa_Bão.md) trong truyền thuyết không phải là thứ mà nhân lực có thể chống lại. Nó là cơn thịnh nộ của trời đất.

Nhưng trong cơn hoảng loạn đó, ta lại thấy một cơ hội.

Nếu Long Cốt đã vỡ, nghĩa là nguồn sức mạnh trấn áp Tây Mạc hàng ngàn năm qua đang vô chủ. Những kẻ gây ra chuyện này chắc chắn đang trọng thương, hoặc đang vật lộn để thoát thân.

Đây không phải là lúc rút lui. Đây là lúc để thu hoạch.

"Rút lui?" Ta cười lạnh, tiếng cười vang lên lanh lảnh giữa tiếng gầm gào của gió bão. "Kẻ yếu mới rút lui. Kẻ mạnh sẽ tìm thấy cơ hội trong hủy diệt."

Ta đưa tay lên, một luồng hắc khí cuộn trào trong lòng bàn tay. *Thiên Tinh Cổ* trong tay áo ta rít lên điên cuồng, nó cũng cảm nhận được nguồn năng lượng khổng lồ đang bùng phát từ tâm bão.

"Nhưng thưa Thánh Tử... Hắc Sa Bão có thể ăn mòn cả xương cốt..."

"Câm miệng!" Ta quát lớn. "Tất cả nghe lệnh! Kết [Vạn Độc Huyết Trận]!"

Đám Huyết Vệ sững sờ trong giây lát, nhưng uy quyền của ta đã in sâu vào tủy xương chúng. Chúng lập tức tản ra, rút dao găm tự rạch tay mình. Máu tươi bắn ra, không rơi xuống đất mà lơ lửng giữa không trung, kết thành một màn chắn màu đỏ thẫm bao quanh chúng ta.

"Tiến vào!" Ta ra lệnh, rồi là người đầu tiên bước về phía bức tường cát đen ngòm đang ập tới.

Gió rít gào bên tai như ngàn vạn oan hồn đang than khóc. Cát đập vào màn chắn huyết trận rào rào. Ta có thể cảm nhận được áp lực khủng khiếp đang đè nặng lên vai, và cả sự ăn mòn tàn bạo của tử khí trong cát.

Nhưng ta không dừng lại.

Mỗi bước đi là một sự đánh cược với tử thần. Nhưng ta thích cảm giác này. Cảm giác đi trên dây, cảm giác nắm giữ vận mệnh của chính mình.

Lâm Phong, Diệp Tĩnh Sương... Hãy cố mà sống sót cho đến khi ta tìm thấy các ngươi. Đừng để [Sa Hồn](../../Kỳ_Vật/Sa_Hồn.md) hay Địa Sát cướp mất con mồi của ta.

Bởi vì cái đầu của các ngươi, và cả bí mật của Long Cốt kia... đều thuộc về Lệ Vô Tâm ta!

Bóng tối nuốt chửng lấy đoàn người nhỏ bé, nhưng ngọn lửa tham vọng trong mắt ta thì rực sáng hơn bao giờ hết, dẫn lối xuyên qua màn đêm vĩnh cửu của sa mạc.
