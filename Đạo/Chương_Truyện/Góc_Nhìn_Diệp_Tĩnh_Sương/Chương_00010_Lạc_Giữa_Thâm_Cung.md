<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00009_Đối_Mặt_Sát_Cơ.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a id="next-chapter-link" href="Chương_00011_Thoát_Khỏi_Địa_Ngục.html">Chương Sau ➡️</a></td>
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
<li style="padding: 5px; "><a href="Chương_00009_Đối_Mặt_Sát_Cơ.html">Chương 9: Đối Mặt Sát Cơ</a></li>
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00010_Lạc_Giữa_Thâm_Cung.html">Chương 10: Lạc Giữa Thâm Cung</a></li>
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
    var nextChapterUrl = "Chương_00011_Thoát_Khỏi_Địa_Ngục.html";

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
# Chương 10: Lạc Giữa Thâm Cung

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Diệp Tĩnh Sương](../../Nhân_Vật/Diệp_Tĩnh_Sương.md)
**Nhân vật liên quan:** [Lâm Phong](../../Nhân_Vật/Lâm_Phong.md), [Hứa Nhược Thủy](../../Nhân_Vật/Hứa_Nhược_Thủy.md)
**Địa điểm:** [Hồ Nguyệt Ảnh](../../Kỳ_Vật/Hồ_Nguyệt_Ảnh.md) - [Hoàng Sa Địa Cung](../../Kỳ_Vật/Hoàng_Sa_Địa_Cung.md).
**Thời điểm:** Song song với [Chương 26: Hoàng Sa Thâm Cung](../Góc_Nhìn_Chính/Chương_00026_Hoàng_Sa_Thâm_Cung.md).
**Giao Điểm Cốt Truyện:** Khoảnh khắc rơi xuống hồ nước ngầm và chiến đấu với Thủy Thi.

---

Cảm giác rơi tự do giữa bóng tối hư vô là thứ đáng sợ nhất. Không có điểm tựa, không có phương hướng, chỉ có tiếng gió rít bên tai và nhịp tim đập thình thịch trong lồng ngực.

*Ùm!*

Cả cơ thể ta va mạnh vào mặt nước lạnh buốt. Cái lạnh thấu xương lập tức xâm nhập vào từng lỗ chân lông, khiến ta tê dại trong khoảnh khắc. Nước tràn vào mũi, vào miệng, mang theo vị mặn chát và mùi tanh tưởi của bùn đất lâu năm.

Ta vùng vẫy, cố gắng ngoi lên mặt nước. Bóng tối bao trùm tất cả, ta không thể nhìn thấy gì, chỉ cảm nhận được dòng nước đang cuộn trào xung quanh.

"Nhược Thủy! Lâm Phong!" Ta hét lên, nhưng tiếng gọi bị nuốt chửng bởi tiếng nước chảy ầm ầm.

Đột nhiên, một luồng ánh sáng xanh lam dịu nhẹ bừng lên từ phía dưới sâu.

Đó là Hứa Nhược Thủy. Nàng đang trôi lơ lửng trong nước, hai mắt nhắm nghiền, nhưng quanh người lại tỏa ra một vầng hào quang kỳ lạ. [Thủy Linh Châu](../../Kỳ_Vật/Thủy_Linh_Châu.md)... Bảo vật gia truyền của nàng đang phản ứng với nguồn nước nơi này.

Nhờ ánh sáng đó, ta nhìn thấy Lâm Phong đang vật lộn cách đó không xa, một tay cố gắng bám vào một tảng đá nhô lên. Và ta cũng nhìn thấy những bóng đen đang lao tới từ phía đáy hồ.

[Thủy Thi](../../Kỳ_Vật/Thủy_Thi.md).

Những xác chết trương phình, da thịt trắng bệch, đôi mắt đục ngầu vô hồn. Chúng bơi trong nước nhanh như cá, móng vuốt sắc nhọn vươn ra, nhắm thẳng vào Hứa Nhược Thủy đang bất động.

"Không được!"

Ta nghiến răng, vận [Hàn Mai Kiếm Quyết](../../Luyện_Khí/Hàn_Ngọc_Kiếm.md). Trong môi trường nước lạnh lẽo này, công pháp của ta như cá gặp nước, uy lực tăng lên gấp bội.

Ta rút kiếm. Dòng nước xung quanh lưỡi kiếm lập tức đông cứng lại thành những mũi băng sắc nhọn.

"Phá!"

Ta vung kiếm chém mạnh xuống nước. Một luồng kiếm khí mang theo hàn băng xé toạc dòng nước, lao thẳng vào đám Thủy Thi.

*Xoẹt! Xoẹt!*

Những mũi băng xuyên thủng cơ thể mềm nhũn của đám xác sống. Máu đen loang ra, hòa vào dòng nước xanh lam tạo nên một cảnh tượng quỷ dị. Nhưng chúng quá đông. Hết con này đến con khác lao tới, không biết sợ hãi, không biết đau đớn.

Ta lặn xuống, bơi nhanh về phía Hứa Nhược Thủy. Một con Thủy Thi đã tiếp cận được nàng, móng vuốt của nó chỉ còn cách cổ nàng vài tấc.

Ta không kịp suy nghĩ, lao tới dùng thân mình che chắn cho nàng.

*Phập!*

Móng vuốt của nó xé rách vai áo ta, cào một đường dài trên da thịt. Cảm giác đau rát ập đến, nhưng cùng với đó là cơn giận dữ bùng lên dữ dội.

"Cút ngay!"

Ta dồn toàn bộ chân khí vào lòng bàn tay, ấn mạnh vào ngực con quái vật.

*Băng Phong Chưởng!*

Cả cơ thể con Thủy Thi lập tức bị bao phủ bởi một lớp băng dày, rồi vỡ tan thành từng mảnh vụn chìm xuống đáy hồ.

Ta nắm lấy tay Hứa Nhược Thủy, kéo nàng ngoi lên mặt nước. Lâm Phong cũng vừa kịp bơi tới, hắn thở hổn hển, tay cầm [Đoản Đao](../../Vũ_Khí/Đoản_Đao.md) dính đầy máu đen.

"Lên bờ! Mau lên bờ!" Hắn hét lớn, chỉ tay về phía một bệ đá rộng lớn ở phía xa, nơi có những bức tượng khổng lồ đứng sừng sững.

Chúng ta dìu nhau bơi về phía đó, vừa bơi vừa chống trả lại những đợt tấn công điên cuồng của đám thủy quái.

Khi chân chạm được vào nền đá lạnh lẽo, ta gần như kiệt sức. Ta ngã gục xuống, hơi thở dồn dập, vết thương trên vai đau nhức nhối. Nhưng khi nhìn sang Hứa Nhược Thủy vẫn an toàn, và Lâm Phong đang cảnh giác canh gác, ta khẽ mỉm cười.

Đây mới chỉ là bắt đầu của Hoàng Sa Địa Cung. Những bí mật đen tối hơn, những cạm bẫy chết người hơn vẫn đang chờ đợi chúng ta ở phía trước. Nhưng chừng nào thanh kiếm này còn trong tay, ta sẽ không để bất cứ ai trong số họ phải nằm lại nơi đáy nước lạnh lẽo này.
