<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00001_Cơ_Duyên_Rừng_Thẳm.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a id="next-chapter-link" href="Chương_00003_Rời_Khỏi_Rừng_Thẳm.html">Chương Sau ➡️</a></td>
</tr>
</table>
<details style="margin-top: 10px;">
<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>
<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">
<li style="padding: 5px; "><a href="Chương_00001_Cơ_Duyên_Rừng_Thẳm.html">Chương 1: Cơ Duyên Rừng Thẳm</a></li>
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00002_Mũi_Tên_Đầu_Tiên.html">Chương 2: Mũi Tên Đầu Tiên</a></li>
<li style="padding: 5px; "><a href="Chương_00003_Rời_Khỏi_Rừng_Thẳm.html">Chương 3: Rời Khỏi Rừng Thẳm</a></li>
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
    var nextChapterUrl = "Chương_00003_Rời_Khỏi_Rừng_Thẳm.html";

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
# Chương 2: Mũi Tên Đầu Tiên

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Lâm Phong](../../Nhân_Vật/Lâm_Phong.md)
**Địa điểm:** Hắc Mộc Lâm (Khu vực trung tâm).
**Thời điểm:** 3 năm sau (Lâm Phong 15 tuổi).
**Giao Điểm Cốt Truyện:** Tuyến độc lập (Quá khứ).

---

Ba năm.

Đối với những cây cổ thụ ngàn năm trong Hắc Mộc Lâm, ba năm chỉ như một cái chớp mắt. Nhưng đối với ta, đó là cả một quá trình lột xác.

Ta, Lâm Phong mười lăm tuổi, giờ đây đã cao hơn hẳn cái đầu, cơ bắp săn chắc cuồn cuộn dưới lớp áo da thú thô sơ. [Truy Phong Cung](../../Luyện_Khí/Truy_Phong_Cung.md) đeo sau lưng đã trở thành một phần cơ thể ta, quen thuộc như hơi thở.

*Vút!*

Ta thả dây cung. Mũi tên gỗ Huyết Đằng xé gió lao đi, ghim chặt con thỏ sừng đang chạy trốn vào gốc cây cách đó trăm bước.

"Luyện Khí Tầng Bốn," ta lẩm bẩm, nhảy xuống từ cành cây cao, thu hồi mũi tên.

Nhờ có *Thanh Mộc Trường Sinh Quyết* và linh khí dồi dào của khu rừng này, tốc độ tu luyện của ta nhanh hơn hẳn so với những gì cuốn bí kíp mô tả. Ta có thể cảm nhận được hơi thở của cây cỏ, nghe được tiếng thì thầm của gió, và nhìn thấy những dòng chảy linh lực mờ ảo trong không khí.

Nhưng hôm nay, khu rừng có gì đó không ổn.

Chim chóc bay tán loạn. Mùi máu tanh nồng nặc bốc lên từ phía thượng nguồn con suối, không phải máu thú, mà là máu người.

Ta nhíu mày, vận *Mộc Độn Thuật*, hòa mình vào tán lá rậm rạp, lướt đi êm ru như một bóng ma.

Đến gần bờ suối, ta nhìn thấy ba gã đàn ông đang vây quanh một cô gái trẻ. Bọn chúng mặc trang phục lôi thôi, tay cầm đao kiếm rỉ sét, nhưng khí tức tỏa ra lại là của tu sĩ.

"Chạy đi đâu hả con ranh?" Tên cầm đầu, một gã mặt sẹo, cười hô hố. "Ngoan ngoãn giao hết dược liệu ra đây, rồi phục vụ bọn gia một đêm, may ra bọn gia tha mạng cho."

Cô gái kia quần áo xộc xệch, tay ôm chặt chiếc giỏ thuốc trước ngực, ánh mắt đầy sợ hãi và tuyệt vọng. Dưới chân cô là xác của một ông lão, ngực bị chém một đao sâu hoắm.

"Lũ khốn nạn! Cha ta... cha ta..." Cô gái nấc lên từng tiếng.

"Lão già đó chết là đáng đời. Ai bảo dám cản đường Tam Hổ bọn ta?" Một tên khác đá mạnh vào cái xác, cười khinh bỉ.

Máu nóng trong người ta sôi lên.

Ba năm qua, ta sống với cầm thú, nhưng chưa từng thấy loài thú nào tàn độc như đám người này. Chúng nó còn không bằng cầm thú.

Ta lặng lẽ rút một mũi tên ra khỏi ống, đặt lên dây cung.

*Bình tĩnh. Lâm Phong, mày chưa từng giết người.*

Một giọng nói vang lên trong đầu ta. Nhưng ngay lập tức, hình ảnh mẹ ta đang nằm liệt giường ở nhà, và ánh mắt tuyệt vọng của cô gái kia đã dập tắt sự do dự đó.

Nếu hôm nay ta không ra tay, ngày mai nạn nhân có thể là mẹ ta, là những người dân làng vô tội của ta.

Ta hít sâu một hơi, để linh lực hệ Mộc tràn vào cánh tay, rồi truyền sang mũi tên. Mũi tên gỗ Huyết Đằng khẽ rung lên, tỏa ra ánh sáng xanh nhạt.

*Truy Phong Tiễn!*

*Vút!*

Tên mặt sẹo đang cười hả hê bỗng im bặt. Hắn trố mắt nhìn xuống ngực mình. Một mũi tên đã xuyên thủng tim hắn từ lúc nào, đuôi tên vẫn còn rung bần bật.

"Đại ca!" Hai tên còn lại hét lên kinh hoàng, quay dáo dác tìm kiếm kẻ tấn công.

"Kẻ nào? Ra đây!"

Ta không trả lời. Ta di chuyển sang một cành cây khác, tiếp tục giương cung.

*Vút!*

Tên thứ hai gục xuống, mũi tên găm thẳng vào cổ họng. Hắn giãy đành đạch vài cái rồi nằm im.

Tên còn lại sợ vỡ mật, vứt cả đao bỏ chạy thục mạng vào rừng.

"Tha mạng! Đại hiệp tha mạng!"

Hắn vừa chạy vừa gào thét. Nhưng hắn không biết rằng, trong Hắc Mộc Lâm này, không ai chạy thoát được *Truy Phong Khách*.

Ta nhảy xuống đất, đuổi theo hắn. Không cần dùng cung nữa. Ta muốn nhìn thẳng vào mắt hắn khi hắn chết.

Ta vận *Mộc Độn*, xuất hiện ngay trước mặt hắn, chặn đường chạy.

"Ngươi... ngươi là ai?" Tên cướp ngã bệt xuống đất, run lẩy bẩy khi nhìn thấy ta - một thiếu niên với đôi mắt lạnh lùng như sói hoang.

"Người đi săn," ta đáp gọn lỏn.

Tay phải ta vung lên. Một dây leo gai góc từ dưới đất trồi lên, quấn chặt lấy cổ hắn, siết mạnh.

*Rắc!*

Tiếng xương gãy giòn tan vang lên giữa khu rừng tĩnh lặng.

Ta buông tay. Cái xác mềm oặt rơi xuống.

Ta đứng đó, nhìn bàn tay mình. Không run rẩy. Không sợ hãi. Chỉ có một cảm giác lạnh lẽo len lỏi trong tim.

Ta đã giết người. Ba mạng người.

Nhưng ta không hối hận.

Ta quay lại bờ suối. Cô gái kia vẫn đang ngồi ôm xác cha khóc nức nở. Thấy ta đi tới, cô sợ hãi lùi lại.

"Đừng sợ," ta nói, giọng khàn khàn. "Ta không hại cô đâu."

Ta để lại cho cô một ít lương khô và chỉ đường về làng gần nhất, rồi lặng lẽ rời đi. Ta không cần sự biết ơn. Ta làm việc này vì chính lương tâm của ta.

Hôm nay, ta đã học được bài học quan trọng nhất của thế giới tu chân: **Kẻ mạnh làm vua, kẻ yếu là mồi.**

Nếu ta muốn bảo vệ gia đình, bảo vệ bản thân, ta phải mạnh hơn nữa. Mạnh đến mức không kẻ nào dám bén mảng đến gần những người ta yêu thương.

Ta siết chặt cây cung trong tay, bóng dáng cô độc khuất dần sau những tán cây đen thẫm. Từ nay, Hắc Mộc Lâm có thêm một thợ săn. Thợ săn những kẻ ác.
