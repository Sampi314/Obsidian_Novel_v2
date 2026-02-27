<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00000_5_Thử_Thách_Đầu_Tiên.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a id="next-chapter-link" href="Chương_00001_5_Dấu_Vết_Tàn_Khốc.html">Chương Sau ➡️</a></td>
</tr>
</table>
<details style="margin-top: 10px;">
<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>
<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">
<li style="padding: 5px; "><a href="Chương_00000_Tuyết_Phủ_Mộ_Phần.html">Chương 0: Tuyết Phủ Mộ Phần</a></li>
<li style="padding: 5px; "><a href="Chương_00000_5_Thử_Thách_Đầu_Tiên.html">Chương 0.5: Thử Thách Đầu Tiên</a></li>
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00001_Nhiệm_Vụ_Đơn_Độc.html">Chương 1: Nhiệm Vụ Đơn Độc</a></li>
<li style="padding: 5px; "><a href="Chương_00001_5_Dấu_Vết_Tàn_Khốc.html">Chương 1.5: Dấu Vết Tàn Khốc</a></li>
<li style="padding: 5px; "><a href="Chương_00002_Hội_Ngộ_Bất_Ngờ.html">Chương 2: Hội Ngộ Bất Ngờ</a></li>
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
    var isStopped = false;

    // Elements to read
    var contentElements = [];

    // Next chapter URL
    var nextChapterUrl = "Chương_00001_5_Dấu_Vết_Tàn_Khốc.html";

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
# Chương 1: Nhiệm Vụ Đơn Độc

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Diệp Tĩnh Sương](../../Nhân_Vật/Diệp_Tĩnh_Sương.md)
**Địa điểm:** Đường biên giới Nam Cương - Cửu Hoa Kiếm Tông.
**Thời điểm:** Trước sự kiện tại Thôn Lạc Diệp (Chương 1 Chính).
**Giao Điểm Cốt Truyện:** [Chương 1: Dấu Hiệu Tai Ương](../Góc_Nhìn_Chính/Chương_00001_Dấu_Hiệu_Tai_Ương.md).

---

Rời khỏi Cửu Hoa Kiếm Tông đã được ba ngày.

Trên con đường mòn dẫn về phía Nam Cương, bóng dáng một nữ tử vận bạch y đơn độc bước đi. Gió thu mang theo hơi lạnh đầu mùa, nhưng dường như còn không lạnh bằng khí tức tỏa ra từ người nàng.

Diệp Tĩnh Sương khẽ chạm tay vào chuôi kiếm [Hàn Mai Kiếm](../../Luyện_Khí/Hàn_Ngọc_Kiếm.md) bên hông. Thanh kiếm này là kỷ vật sư phụ để lại, cũng là người bạn đồng hành duy nhất của nàng trong suốt những năm tháng tu đạo cô độc.

"Tĩnh Sương, tâm ngươi quá lạnh."

Lời nhận xét của Tông Chủ Lục Trần khi giao nhiệm vụ này cho nàng vẫn còn văng vẳng bên tai.

"Kiếm đạo của Cửu Hoa Kiếm Tông ta tuy sắc bén, nhưng không vô tình. Ngươi tu luyện *Hàn Sương Kiếm Quyết*, lấy băng giá làm cốt, nhưng nếu để tâm hồn cũng đóng băng, e rằng sẽ đi vào ngõ cụt."

Nàng nhớ lại ánh mắt lo lắng của Tông Chủ. Người đã phái nàng đi điều tra vụ mất tích của đoàn thương buôn Thiên Sa Thương Hội, không chỉ vì năng lực của nàng, mà có lẽ còn muốn nàng ra ngoài trần thế, tìm kiếm chút "hơi ấm" của nhân gian.

"Hơi ấm sao?"

Diệp Tĩnh Sương cười nhạt, một nụ cười chua chát thoáng qua trên môi.

Với nàng, hơi ấm là thứ xa xỉ đã chết cùng quá khứ. Kể từ ngày gia đình bị sát hại, trái tim nàng đã sớm bị chôn vùi dưới lớp băng tuyết vĩnh cửu.

*Sư phụ... người có thấy không?*

Trong tâm trí nàng bỗng hiện lên hình ảnh người thầy quá cố. Những bông tuyết đầu mùa bắt đầu rơi lả tả, đậu trắng xóa trên vai áo nàng, lạnh buốt như chính tâm can lúc này. Nàng nhớ sư phụ từng dạy: *"Kiếm của người tu đạo, sắc bén ở lưỡi, nhưng phải ấm áp ở chuôi. Nếu lòng người cầm kiếm cũng lạnh như sắt thép, thì đó chỉ là công cụ giết chóc, không phải là Đạo."*

Nàng đã luôn khắc cốt ghi tâm lời dạy ấy. Nhưng làm sao nàng có thể giữ cho lòng mình ấm áp khi mà mỗi đêm nhắm mắt lại, hình ảnh cha mẹ nằm trên vũng máu, hình ảnh cả thôn làng chìm trong biển lửa vẫn cứ hiện về như một cơn ác mộng không hồi kết?

Huyết Sát Minh... Vạn Độc Môn... những cái tên ấy như những mũi dao găm vào tim nàng mỗi ngày. Chúng cướp đi gia đình nàng, cướp đi tuổi thơ, và cướp đi cả nụ cười của người con gái tên Tĩnh Sương ngày nào.

Người đời nói nàng có tư chất ngàn năm có một, sinh ra là để làm bạn với kiếm. Nàng đã luyện *Hàn Sương Kiếm Quyết* đến tầng thứ bảy, có thể đóng băng cả một dòng sông đang chảy xiết. Nhưng nàng lại bất lực, không thể đóng băng được ngọn lửa hận thù đang thiêu đốt tâm can mình.

Mỗi lần rút kiếm, nàng thấy mình như đang múa trên lưỡi dao. Một bên là Đạo, là sự từ bi, là bảo vệ kẻ yếu mà Cửu Hoa Kiếm Tông tôn thờ. Một bên là Ma, là sự tàn nhẫn, là khát vọng trả thù đến cùng cực.

*Con sợ... con sợ một ngày nào đó, con sẽ lạc lối. Con sợ thanh Hàn Mai Kiếm này sẽ không còn là kiếm của chính nghĩa, mà trở thành kiếm của ma đạo.*

Tông Chủ bảo nàng đi tìm "hơi ấm nhân gian". Nhưng nhân gian này liệu có còn hơi ấm nào dành cho nàng không? Hay chỉ toàn là lừa lọc, phản bội và máu tanh?

Nàng tu kiếm không phải để tìm kiếm đại đạo, mà để có sức mạnh bảo vệ những gì còn sót lại, và trừng phạt cái ác. Nếu nàng không thể trở về sau nhiệm vụ này, nàng chỉ mong sư phụ tha thứ cho đứa đệ tử bất hiếu. Nàng không sợ chết. Nàng chỉ sợ chết đi mà chưa trả được thù, chưa diệt sạch lũ tà ma ngoại đạo kia.

Càng đi sâu về phía Nam, cảnh vật càng trở nên hoang vu. Những cánh rừng lá kim thưa thớt dần, nhường chỗ cho những dãy núi đá vôi lởm chởm. Mùi thảo mộc đặc trưng của Dược Vương Cốc thoang thoảng trong gió, nhưng hôm nay, nó có gì đó khác lạ.

Diệp Tĩnh Sương dừng lại bên một con suối nhỏ để rửa mặt. Dòng nước trong vắt phản chiếu gương mặt thanh tú nhưng vô cảm của nàng.

Bỗng nhiên, mặt nước xao động.

Một chiếc lá đỏ trôi theo dòng nước, dập dềnh rồi mắc vào khe đá ngay trước mặt nàng. Không phải lá phong. Màu đỏ ấy... là máu.

Ánh mắt Diệp Tĩnh Sương lập tức sắc lại. Nàng ngẩng đầu nhìn về phía thượng nguồn. Nơi đó, mây đen đang tụ lại thành từng khối nặng nề, che khuất ánh mặt trời buổi sớm.

"Có mùi máu tanh..."

Nàng lẩm bẩm, đứng dậy, thân hình bỗng chốc trở nên nhẹ bẫng. Vận dụng khinh công, nàng lướt đi trên ngọn cỏ, hướng thẳng về phía Thôn Lạc Diệp - điểm dừng chân cuối cùng của đoàn thương buôn trước khi mất tích.

Trong lòng nàng dấy lên một linh cảm chẳng lành. Sự yên tĩnh của khu rừng này quá bất thường. Không tiếng chim hót, không tiếng thú chạy. Chỉ có tiếng gió rít qua khe đá như tiếng than khóc của oan hồn.

Khi bóng dáng ngôi làng hiện ra dưới thung lũng, Diệp Tĩnh Sương dừng lại trên một mỏm đá cao, tà áo trắng bay phần phật trong gió.

Nàng nheo mắt nhìn xuống. Thôn Lạc Diệp nằm im lìm trong sương sớm, nhưng cái im lìm ấy sặc mùi tử khí.

"Quá yên tĩnh," nàng tự nói với chính mình.

Bàn tay nàng siết chặt chuôi kiếm. Nhiệm vụ đơn độc này, e rằng sẽ không đơn giản như nàng nghĩ. Và lời dạy của Tông Chủ về "hơi ấm nhân gian", có lẽ phải gác lại sau. Trước mắt nàng bây giờ, chỉ có lạnh lẽo và máu tanh.

Gió lạnh quá. Nhưng nàng không thấy lạnh. Vì tim nàng... đã đóng băng từ lâu rồi.

Diệp Tĩnh Sương hít sâu một hơi, để luồng chân khí lạnh lẽo lưu chuyển khắp kinh mạch, sẵn sàng cho một cuộc tàn sát.

Nàng nhún người, lao xuống thung lũng, bước vào cơn ác mộng đang chờ đợi.
