<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00001_Nhiệm_Vụ_Đơn_Độc.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a href="Chương_00002_Hội_Ngộ_Bất_Ngờ.html">Chương Sau ➡️</a></td>
</tr>
</table>
<details style="margin-top: 10px;">
<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>
<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">
<li style="padding: 5px; "><a href="Chương_00000_Tuyết_Phủ_Mộ_Phần.html">Chương 0: Tuyết Phủ Mộ Phần</a></li>
<li style="padding: 5px; "><a href="Chương_00000_5_Thử_Thách_Đầu_Tiên.html">Chương 0.5: Thử Thách Đầu Tiên</a></li>
<li style="padding: 5px; "><a href="Chương_00001_Nhiệm_Vụ_Đơn_Độc.html">Chương 1: Nhiệm Vụ Đơn Độc</a></li>
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00001_5_Dấu_Vết_Tàn_Khốc.html">Chương 1.5: Dấu Vết Tàn Khốc</a></li>
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
  <button onclick="speakChapter()" style="cursor: pointer; padding: 5px 10px; margin: 5px;">▶️ Đọc</button>
  <button onclick="pauseSpeech()" style="cursor: pointer; padding: 5px 10px; margin: 5px;">⏸️ Tạm Dừng</button>
  <button onclick="resumeSpeech()" style="cursor: pointer; padding: 5px 10px; margin: 5px;">⏯️ Tiếp Tục</button>
  <button onclick="stopSpeech()" style="cursor: pointer; padding: 5px 10px; margin: 5px;">⏹️ Dừng</button>
</div>
<script>
var synth = window.speechSynthesis;
var utterance = null;

function speakChapter() {
  if (synth.speaking) {
    console.error("speechSynthesis.speaking");
    return;
  }
  // Clone body to remove navigation before reading
  var content = document.body.cloneNode(true);
  var nav = content.querySelector("#chapter-navigation");
  if (nav) {
    nav.remove();
  }
  var text = content.innerText;
  utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "vi-VN";
  synth.speak(utterance);
}

function pauseSpeech() {
  if (synth.speaking && !synth.paused) {
    synth.pause();
  }
}

function resumeSpeech() {
  if (synth.paused) {
    synth.resume();
  }
}

function stopSpeech() {
  if (synth.speaking) {
    synth.cancel();
  }
}
</script>
</div>
<!-- NAVIGATION_END -->
# Chương 1.5: Dấu Vết Tàn Khốc

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Diệp Tĩnh Sương](../../Nhân_Vật/Diệp_Tĩnh_Sương.md)
**Địa điểm:** Đường mòn ven rừng Vĩnh Hằng Sâm Lâm - Gần Thôn Lạc Diệp.
**Thời điểm:** Giữa Chương 1 và trước khi đến Thôn Lạc Diệp.
**Giao Điểm Cốt Truyện:** Tuyến độc lập.

---

Cơn mưa rừng bất chợt đổ xuống, nặng hạt và lạnh buốt như ngàn mũi kim châm vào da thịt. Nhưng Diệp Tĩnh Sương vẫn không dừng bước. Tà áo trắng của nàng ướt đẫm, bám sát vào thân hình mảnh mai, nhưng đôi mắt phượng vẫn kiên định nhìn về phía trước, xuyên qua màn mưa trắng xóa.

Mùi máu tanh mà nàng ngửi thấy ở thượng nguồn con suối ban nãy càng lúc càng nồng nặc, hòa lẫn với mùi ẩm mốc của lá mục và... một mùi gì đó khác lạ. Mùi hăng hắc, ngọt lợ, khiến người ta buồn nôn.

Đó là mùi của Độc Dược.

"Chết tiệt!"

Diệp Tĩnh Sương rủa thầm, vận *Hàn Sương Kiếm Quyết* lên mức cao nhất, tạo thành một lớp màn chắn vô hình xung quanh cơ thể, ngăn cách nước mưa và độc khí.

Nàng lao đi như một tia chớp trắng, bỏ lại sau lưng những vũng nước bắn tung tóe.

Chỉ lát sau, một cảnh tượng kinh hoàng hiện ra trước mắt nàng.

Một ngôi làng nhỏ, chỉ chừng mười mấy nóc nhà, nằm lọt thỏm giữa thung lũng. Nhưng giờ đây, nó đã biến thành một bãi tha ma.

Khói đen bốc lên nghi ngút từ những mái nhà tranh đang cháy dở. Xác người nằm la liệt khắp nơi, từ sân nhà ra đến ngõ xóm. Già trẻ, lớn bé, không một ai sống sót.

Điều đáng sợ nhất là cái chết của họ.

Tất cả đều có làn da tím tái, thất khiếu chảy máu đen, cơ thể co quắp trong đau đớn tột cùng. Một số cái xác thậm chí còn đang rỉ ra thứ chất lỏng màu xanh lục, bốc mùi hôi thối nồng nặc.

"Vạn Độc Môn..."

Diệp Tĩnh Sương nghiến răng, tay siết chặt chuôi kiếm đến mức đốt ngón tay trắng bệch. Nàng nhận ra thủ đoạn tàn độc này. Chính là lũ súc sinh đó.

Nàng bước chậm rãi vào ngôi làng chết chóc. Mỗi bước chân như đeo chì.

Một người phụ nữ ôm chặt đứa con nhỏ trong lòng, cả hai đều đã chết cứng. Đứa trẻ vẫn còn ngậm chặt núm vú mẹ, nhưng thay vì sữa, thứ chảy vào miệng nó là máu độc.

Diệp Tĩnh Sương quỳ xuống, nhẹ nhàng vuốt mắt cho hai mẹ con. Một giọt nước mắt lăn dài trên má nàng, hòa vào nước mưa mặn chát.

"Xin lỗi... ta đến muộn rồi."

Nàng đứng dậy, ánh mắt rực lửa hận thù. Nàng rút thanh *Hàn Mai Kiếm* ra. Lưỡi kiếm sáng loáng phản chiếu ánh chớp xẹt ngang bầu trời, lạnh lẽo đến thấu xương.

*Bọn chúng chưa đi xa.*

Nàng cảm nhận được tàn dư linh lực của kẻ thi triển độc thuật vẫn còn vương lại trong không khí. Một luồng khí tức âm hàn, tà ác, đang hướng về phía Đông Nam.

Phía Đông Nam... đó là hướng đi về Thôn Lạc Diệp.

"Thôn Lạc Diệp!"

Tim Diệp Tĩnh Sương thắt lại. Nếu bọn chúng đang hướng về đó, thì ngôi làng kia...

Không chần chừ thêm một giây nào nữa, nàng vận toàn lực, lao đi như một mũi tên xé gió.

*Ta thề, ta sẽ bắt các ngươi phải trả giá. Máu nợ máu!*

Gió gào thét bên tai nàng như tiếng oan hồn đòi mạng. Mưa quất vào mặt nàng rát buốt. Nhưng trong lòng Diệp Tĩnh Sương giờ đây chỉ có một ngọn lửa duy nhất đang bùng cháy dữ dội: Ngọn lửa của sự trừng phạt.

Con đường tu tiên của nàng có thể cô độc, có thể lạnh lẽo, nhưng nàng tuyệt đối sẽ không để cái ác lộng hành ngay trước mắt mình.

Thanh kiếm trong tay nàng rung lên bần bật, như cảm nhận được sát ý ngút trời của chủ nhân. Nó đang khát máu. Máu của những kẻ thủ ác.
