<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px; color: #adb5bd;">⬅️ Chương Trước</td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a href="Chương_00000_5_Thử_Thách_Đầu_Tiên.html">Chương Sau ➡️</a></td>
</tr>
</table>
<details style="margin-top: 10px;">
<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>
<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00000_Tuyết_Phủ_Mộ_Phần.html">Chương 0: Tuyết Phủ Mộ Phần</a></li>
<li style="padding: 5px; "><a href="Chương_00000_5_Thử_Thách_Đầu_Tiên.html">Chương 0.5: Thử Thách Đầu Tiên</a></li>
<li style="padding: 5px; "><a href="Chương_00001_Nhiệm_Vụ_Đơn_Độc.html">Chương 1: Nhiệm Vụ Đơn Độc</a></li>
<li style="padding: 5px; "><a href="Chương_00001_5_Dấu_Vết_Tàn_Khốc.html">Chương 1.5: Dấu Vết Tàn Khốc</a></li>
<li style="padding: 5px; "><a href="Chương_00002_Hội_Ngộ_Bất_Ngờ.html">Chương 2: Hội Ngộ Bất Ngờ</a></li>
<li style="padding: 5px; "><a href="Chương_00003_Lời_Thề_Kiếm_Khách.html">Chương 3: Lời Thề Kiếm Khách</a></li>
<li style="padding: 5px; "><a href="Chương_00004_Lạc_Giữa_Thâm_Cung.html">Chương 4: Lạc Giữa Thâm Cung</a></li>
<li style="padding: 5px; "><a href="Chương_00005_Thoát_Khỏi_Địa_Ngục.html">Chương 5: Thoát Khỏi Địa Ngục</a></li>
<li style="padding: 5px; "><a href="Chương_00006_Quyết_Định_Sinh_Tử.html">Chương 6: Quyết Định Sinh Tử</a></li>
<li style="padding: 5px; "><a href="Chương_00007_Đối_Mặt_Sát_Cơ.html">Chương 7: Đối Mặt Sát Cơ</a></li>
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
# Chương 0: Tuyết Phủ Mộ Phần

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Diệp Tĩnh Sương](../../Nhân_Vật/Diệp_Tĩnh_Sương.md)
**Địa điểm:** Núi Tuyết (Biên giới Đông Hoang).
**Thời điểm:** 10 năm trước (Diệp Tĩnh Sương 15 tuổi).
**Giao Điểm Cốt Truyện:** Tuyến độc lập (Quá khứ).

---

Mùa đông năm nay đến sớm. Gió Bắc mang theo tuyết rơi dày đặc, phủ trắng xóa cả dãy núi trùng điệp.

Trong một hang động nhỏ khuất sau vách đá dựng đứng, ánh lửa bập bùng soi rõ hai bóng người. Một già, một trẻ.

Lão nhân gầy gò, tóc bạc trắng như cước, đang ngồi tựa lưng vào vách đá lạnh lẽo. Hơi thở của ông yếu ớt, đứt quãng như ngọn đèn trước gió. Trên ngực áo ông loang lổ vết máu đen thẫm – dấu tích của trận chiến với [Huyết Sát Minh](../../Thế_Lực/Huyết_Sát_Minh.md) ba ngày trước.

"Sư phụ..."

Thiếu nữ mười lăm tuổi quỳ bên cạnh, đôi mắt đỏ hoe, tay nắm chặt bàn tay nhăn nheo lạnh ngắt của người thầy. Nàng mặc một bộ y phục vá víu nhưng sạch sẽ, mái tóc đen dài được buộc gọn bằng một dải lụa trắng.

"Đừng khóc, Tĩnh Sương." Lão nhân thì thào, giọng khàn đặc. "Khóc lóc là việc của kẻ yếu đuối. Kiếm khách... phải biết nuốt nước mắt vào trong."

"Nhưng... con không muốn người đi..." Diệp Tĩnh Sương nấc lên, nước mắt lăn dài trên gò má trắng ngần.

Cổ Kiếm Mạc đưa tay lên, định lau nước mắt cho đệ tử nhưng cánh tay ông run rẩy rồi rơi xuống. Ông mỉm cười yếu ớt.

"Ta sống đến tuổi này, tung hoành ngang dọc một đời, cũng coi như không uổng phí. Chỉ tiếc là... chưa kịp nhìn thấy con trưởng thành, chưa kịp thấy con dương danh thiên hạ."

Ông ho khan một tràng dài, mỗi tiếng ho như rút đi chút sinh lực cuối cùng. Máu tươi trào ra khóe miệng.

"Tĩnh Sương, nghe ta dặn đây." Ông cố gắng gượng dậy, ánh mắt bỗng trở nên nghiêm nghị lạ thường.

Diệp Tĩnh Sương vội vàng lau nước mắt, chăm chú lắng nghe.

"Thanh [Hàn Mai Kiếm](../../Luyện_Khí/Hàn_Ngọc_Kiếm.md) này... là bảo vật cả đời ta tích góp được. Nay ta truyền lại cho con. Hãy nhớ kỹ lời ta dạy: Kiếm của người tu đạo, không được dùng để ức hiếp kẻ yếu, nhưng tuyệt đối không được nương tay với kẻ ác. Lòng nhân từ với kẻ thù chính là tàn nhẫn với bản thân."

Ông run rẩy tháo thanh kiếm vỏ trắng bên hông xuống, đặt vào tay nàng. Thanh kiếm nặng trĩu, tỏa ra hơi lạnh buốt giá.

"Con xin nghe lời sư phụ dạy bảo," Diệp Tĩnh Sương cúi đầu nhận lấy, giọng nghẹn ngào.

"Còn nữa... *Hàn Sương Kiếm Quyết*... con đã luyện đến tầng thứ năm. Nhưng muốn đạt đến đại thành, con phải nhớ một điều: Tâm như băng, ý như sương. Đừng để hận thù làm mờ mắt, nhưng hãy dùng nó làm động lực để vươn lên."

Cổ Kiếm Mạc nhìn đệ tử lần cuối, ánh mắt chan chứa yêu thương và kỳ vọng.

"Hãy đi đi... Hãy đi tìm Cửu Hoa Kiếm Tông. Chỉ có nơi đó mới đủ sức che chở và bồi dưỡng con thành tài. Hãy nói với Tông Chủ Lục Trần... rằng Cổ Kiếm Mạc gửi gắm đứa trẻ này..."

Giọng ông nhỏ dần rồi tắt hẳn. Đôi mắt từ từ khép lại, bàn tay buông lỏng.

"Sư phụ!!!"

Tiếng hét xé lòng của Diệp Tĩnh Sương vang vọng khắp núi rừng hoang vu. Nàng ôm lấy thi thể người thầy, khóc nức nở như một đứa trẻ lạc mất cha mẹ lần thứ hai trong đời.

***

Ba ngày sau.

Bão tuyết đã ngừng rơi, nhưng cái lạnh vẫn cắt da cắt thịt.

Trước cửa hang động giờ đây mọc lên một nấm mộ mới đắp bằng đá núi. Không bia đá cầu kỳ, chỉ có một phiến đá thô sơ khắc ba chữ nguệch ngoạc bằng kiếm khí: *Cổ Kiếm Mạc*.

Diệp Tĩnh Sương đứng trước mộ, trên người mặc bộ đồ tang trắng toát. Gió thổi tung mái tóc đen dài, để lộ khuôn mặt thanh tú nhưng lạnh lùng đến đáng sợ. Đôi mắt nàng không còn vương chút nước mắt nào nữa, thay vào đó là sự kiên định và băng giá.

Nàng rút thanh Hàn Mai Kiếm ra khỏi vỏ. Lưỡi kiếm sáng loáng phản chiếu ánh mặt trời mùa đông yêu ớt.

"Sư phụ, người yên nghỉ nhé. Mối thù của cha mẹ, mối thù của người... con xin thề sẽ trả đủ."

Nàng cắm phập thanh kiếm xuống đất, quỳ xuống lạy ba lạy trước mộ thầy.

Khi đứng dậy, Diệp Tĩnh Sương không ngoảnh đầu lại nữa. Nàng khoác tay nải lên vai, bước đi dứt khoát về phía Đông. Bóng dáng nhỏ bé cô độc giữa đất trời mênh mông tuyết trắng, nhưng bước chân lại vững chãi hơn bao giờ hết.

Kể từ ngày hôm đó, cô bé hay khóc nhè trong vòng tay sư phụ đã chết theo người thầy quá cố. Trên đời này chỉ còn lại một Diệp Tĩnh Sương, một *Hàn Mai Kiếm* lạnh lùng, vô tình, sẵn sàng chém đứt mọi bất công ngang trái trên thế gian này.

Tuyết lại bắt đầu rơi, che lấp những dấu chân cô độc trên con đường tu tiên đầy chông gai phía trước.
