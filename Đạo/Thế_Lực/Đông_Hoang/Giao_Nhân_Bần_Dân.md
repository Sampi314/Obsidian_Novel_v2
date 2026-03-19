---
type: faction
name: Giao Nhân Bần Dân
hantu: 鲛人贫民
faction_type: Bộ Lạc
alignment: -2
race: Giao Nhân Tộc
region: Đông Hoang
founded: Từ thuở sơ khai Giao Nhân Tộc
founder: Không có (giai cấp tự nhiên hình thành)
emblem: Giao_Nhan_Ban_Dan.png
specialty: Dệt ti biển, Sản xuất ngọc trai nước mắt, Lao động thủ công dưới nước
economy:
- Dệt ti biển cho hoàng tộc
- Ngọc trai nước mắt (bị hoàng tộc thu hết)
- Lao động khổ sai đổi lương thực
arcs:
  - arc: 1
    status: Bị áp bức
    rank: Không Xếp Hạng
    leader: Trưởng Khu Lệ Vân
    population: 200
    territory:
      - Khu ổ chuột rìa ngoài lãnh hải Lệ Nhược Thủy
    assets:
      - name: Xưởng Dệt Ti Biển
        type: Công Trình
      - name: Hắc Ngọc Trai (bí mật)
        type: Bảo Vật
    stats: [5, 10, 5, 200, 5, 5]
    divisions:
      - name: Khu Bần Dân
        role: Sinh sống và lao động dệt ti biển cho hoàng tộc
        headcount:
          truong_lao: 1
          chien_binh: 0
          dan_thuong: 199
        members:
          - character: Lệ Vân
            position: Trưởng Khu
            cultivation: Trúc Cơ (tự học, giấu kín)
          - character: "[Bé Gái Hắc Ngọc]"
            position: Dân thường
            cultivation: Không
            placeholder: true
    relationships:
      - faction: Giao Nhân Hoàng Tộc
        description: Giai cấp bị áp bức và bóc lột, bần dân bị cấm rời khu vực mà không có giấy phép, ngọc trai nước mắt bị thu hết.
        diplomacy:
          lien_minh: -80
          tin: -60
          uy_hiep: 90
          thuong_mai: -90
          on_oan: -70
          le_thuoc: 95
      - faction: Giao Nhân Tộc Liên Minh
        description: Lệ Vân bí mật liên lạc với liên minh bên ngoài, tìm cách giải phóng bần dân khỏi ách thống trị.
        diplomacy:
          lien_minh: 40
          tin: 30
          uy_hiep: 0
          thuong_mai: 0
          on_oan: 50
          le_thuoc: 0
      - faction: Ngọc Trai Sâu Phường
        description: Phường thu mua ngọc trai thông qua hoàng tộc, gián tiếp hưởng lợi từ sức lao động bần dân, bần dân căm ghét nhưng bất lực.
        diplomacy:
          lien_minh: -30
          tin: -20
          uy_hiep: 20
          thuong_mai: -50
          on_oan: -40
          le_thuoc: 30
---

# Giao Nhân Bần Dân (鲛人贫民)

> *"Sinh ra đã khóc, chết đi vẫn khóc — nhưng một ngày, nước mắt sẽ hóa thành lửa."*
> — Bài hát ru cổ lưu truyền trong khu bần dân, tương truyền là di ngôn của Lệ Huyết

> *"Mười ngón tay chai sần dệt nên tấm vải vương giả, nhưng kẻ dệt không đủ vải che thân."*
> — Lệ Vân, nói với bà Mẫu Châu trong đêm mưa

## I. Tổng Quan (总览)
Giao Nhân Bần Dân không phải một thế lực theo nghĩa truyền thống mà là một giai cấp bị đè nén trong xã hội Giao Nhân Tộc. Khoảng hai trăm Giao Nhân sống chen chúc trong khu ổ chuột tồi tàn ở rìa ngoài lãnh hải Lệ Nhược Thủy, bị cấm tự do đi lại và phải lao động cực nhọc dệt ti biển cho tầng lớp hoàng tộc. Nước mắt họ hóa thành ngọc trai nhưng họ không được phép giữ lại một viên nào — hoàng tộc gọi đó là "thuế lệ," một cách nói hoa mỹ cho sự cướp bóc trắng trợn. Trưởng Khu Lệ Vân, một Giao Nhân già cảnh giới tương đương Trúc Cơ nhờ tự học, âm thầm giữ ngọn lửa phản kháng cháy âm ỉ trong lòng khu bần dân, chờ đợi thời cơ thay đổi số phận của cả cộng đồng. Dưới vẻ ngoài cam chịu, bần dân đang chuẩn bị cho một cuộc di tản bí mật mà nếu thất bại, cái giá phải trả sẽ là toàn bộ hai trăm mạng người.

## II. Địa Lý & Tài Nguyên (地理与资源)
Khu bần dân nằm ở vùng rìa ngoài lãnh hải Giao Nhân hoàng tộc, tại một khu vực đáy biển trũng sâu gọi là Lệ Oa — "Hố Nước Mắt" — nơi dòng hải lưu lạnh và ánh sáng mặt trời hiếm khi xuyên tới. Nhà cửa được xây bằng xương cá lớn và rong biển ép chặt, chật chội, tối tăm, và luôn ẩm mốc — tường nhà phủ rêu xanh đen, mùi tanh hôi không bao giờ dứt. Các gia đình sáu bảy người chen chung trong những căn phòng chỉ rộng vài thước vuông, trẻ con ngủ chồng lên nhau trên sàn rong biển ướt. Khu vực được bao quanh bởi ba trạm canh của Lệ Vệ — lực lượng an ninh hoàng tộc — canh gác ngày đêm, mỗi trạm có hai Giao Nhân chiến binh Trúc Cơ đảm bảo không ai ra vào trái phép. Trạm canh phía bắc mang tên Giám Lệ Đài, có tháp quan sát cao nhất nhìn thẳng xuống toàn bộ khu bần dân. Tài nguyên duy nhất đáng kể là ti biển — loại tơ do Giao Nhân tiết ra từ tuyến dịch dưới da, mềm mại và bền hơn bất kỳ loại tơ nào trên cạn. Tuy nhiên, toàn bộ sản phẩm ti biển đều bị hoàng tộc thu hết, bần dân chỉ nhận lại lương thực tối thiểu đủ để sống sót và tiếp tục lao động — mỗi ngày mỗi người được phát hai nắm tảo khô và một con cá muối nhỏ.

## III. Văn Hóa & Tín Ngưỡng (文化与信仰)
Văn hóa bần dân thấm đẫm nỗi buồn truyền đời, nhưng trong nỗi buồn đó ẩn chứa một sức sống kiên cường đáng kinh ngạc. Câu nói "Sinh ra đã khóc, chết đi vẫn khóc" không chỉ là thành ngữ mà là sự thật hiện thực — nước mắt Giao Nhân hóa ngọc trai, và trong khu bần dân, không thiếu nước mắt. Trẻ em bắt đầu dệt ti biển từ năm tuổi, mười ngón tay chai sần là dấu hiệu nhận biết kẻ thuộc giai cấp dưới đáy — hoàng tộc gọi đó là "Thập Chỉ Ấn," dấu vết vĩnh viễn không bao giờ phai. Hoàng tộc tuyên truyền rằng ngọc trai từ nước mắt bần dân có màu xám đục vì "tâm hồn không thuần khiết", nhưng sự thật là do cơ thể bần dân kiệt sức và suy dinh dưỡng trầm trọng. Dù trong cảnh khốn cùng, bần dân vẫn lưu truyền những bài hát ru bằng thứ tiếng Giao Nhân cổ mà hoàng tộc đã bỏ quên — trong các bài hát ấy ẩn chứa ký ức về thời kỳ Giao Nhân chưa phân chia giai cấp. Bài hát quan trọng nhất mang tên "Lệ Hỏa Ca" — khúc ca về nước mắt hóa lửa — được các bà mẹ hát rất nhỏ cho con nghe mỗi đêm, truyền lại lời nguyền giải phóng từ thế hệ này sang thế hệ khác. Ngoài ra, trẻ em bần dân có phong tục "Lệ Giao" — khi hai đứa trẻ thân thiết cùng khóc và trao đổi ngọc trai cho nhau, coi đó là lời thề kết nghĩa mạnh hơn máu mủ.

## IV. Cơ Cấu Tổ Chức (组织结构)
Khu bần dân không có tổ chức chính thức, chỉ có Trưởng Khu do hoàng tộc chỉ định để phân công lao động. Lệ Vân đảm nhiệm vai trò này, một Giao Nhân già tóc bạc trắng, lưng còng, đi lại chậm chạp — vẻ ngoài mà hoàng tộc coi là ngoan ngoãn và vô hại. Thực tế lão là hậu duệ trực hệ của Lệ Huyết, người lãnh đạo cuộc nổi dậy hai trăm năm trước, mang trong lòng thù hận ngầm qua bảy thế hệ không nguôi. Dưới lão là năm mươi Thợ Dệt chính thức cảnh giới Luyện Khí, làm việc mười hai canh giờ mỗi ngày không ngừng nghỉ — trong đó có bảy người là tai mắt bí mật của Lệ Vân, được lão âm thầm chỉ dạy một vài chiêu thức tự vệ cơ bản. Phần còn lại gồm người già, trẻ em, và những Giao Nhân quá yếu để dệt — họ làm các việc lặt vặt như thu hoạch rong biển, nấu ăn, và chăm sóc người bệnh. Bà Mẫu Châu, Giao Nhân già nhất khu bần dân ở tuổi ba trăm, là người duy nhất ngoài Lệ Vân biết toàn bộ kế hoạch di tản — bà giữ vai trò "bà đỡ" và "bà lang" cho cả khu, sinh vật duy nhất mà ngay cả Lệ Vệ cũng nể mặt vì không ai muốn tự tay đỡ đẻ cho bần dân.

## V. Công Pháp & Trận Pháp (功法与阵法)
Bần dân bị hoàng tộc cấm tuyệt đối không được tu luyện công pháp chiến đấu — bất kỳ ai bị phát hiện tự tu luyện sẽ bị cắt tuyến dịch ti biển vĩnh viễn, trở thành "Phế Nhân" mất khả năng lao động, bị bỏ rơi cho đến chết. Kỹ thuật duy nhất được phép học là Phưởng Ti Thuật — phương pháp kéo tơ từ tuyến dịch dưới da, thuần túy phục vụ sản xuất, được dạy bởi các Giám Công hoàng tộc một cách nghiêm ngặt và không cho phép biến đổi. Tuy nhiên, Lệ Vân đã bí mật tự học được Thủy Lưu Thuật từ một mảnh sách rách nhặt được trong đống rác hoàng tộc vứt bỏ — mảnh sách chỉ chứa nửa bộ công pháp, nhưng lão đã tự mò mẫm bổ sung nửa còn lại qua năm mươi năm thử nghiệm, bằng cách quan sát dòng chảy tự nhiên của hải lưu lạnh quanh Lệ Oa và mô phỏng lại bằng linh lực. Lão luyện tập vào ban đêm khi không ai quan sát, tại một hốc đá nhỏ dưới nền Xưởng Dệt, và đã đạt cảnh giới tương đương Trúc Cơ. Nếu bị hoàng tộc phát hiện tu luyện trái phép, Lệ Vân sẽ bị xử tử làm gương, vì vậy lão che giấu vô cùng cẩn thận — ngay cả những bần dân thân cận nhất cũng chỉ cảm nhận được rằng lão "khỏe hơn bình thường", không ai biết thực lực thực sự.

## VI. Đặc Sản Môn Phái (门派特产)
**Ti Biển Giao Nhân** là loại tơ mềm mại, bền bỉ và có ánh ngọc trai nhẹ, được giới quyền quý khắp Đông Hoang săn đón — một tấm vải ti biển thượng hạng bán giá năm trăm linh thạch hạ phẩm ở chợ Bách Nghệ Phường, nhưng người dệt ra nó chỉ nhận lại hai nắm tảo khô. Ti biển loại tốt nhất — "Nguyệt Quang Ti" — dệt bởi thợ lành nghề nhất, có khả năng phát sáng nhạt dưới trăng, được hoàng tộc dành riêng cho lễ phục cung đình. Toàn bộ sản phẩm bị hoàng tộc thu giữ và bán qua Ngọc Trai Sâu Phường với giá cao ngất, bần dân không nhận được xu nào. **Ngọc Trai Nước Mắt Xám** kết tinh từ nước mắt bần dân, có màu xám đục do cơ thể suy kiệt — hoàng tộc gọi chúng là "Trọc Lệ Châu" và bán rẻ hơn ngọc trai hoàng tộc, nhưng các dược sư phát hiện rằng Trọc Lệ Châu chứa một loại dược tính đặc biệt: khi nghiền thành bột pha vào đan dược, nó có tác dụng trấn an tâm thần mạnh mẽ bất thường, có lẽ vì kết tinh từ nỗi đau thực sự. **Bài Hát Ru Cổ** không phải sản phẩm vật chất nhưng là di sản văn hóa quý giá, lưu giữ tiếng Giao Nhân cổ mà hoàng tộc đã quên, trong đó ẩn chứa các giai điệu có tác dụng an thần dưới nước — đặc biệt bài "Lệ Hỏa Ca" mà nếu hát đúng âm vực cổ, có thể kích hoạt cộng hưởng linh lực trong nước biển xung quanh.

## VII. Cơ Sở Hạ Tầng (基础设施)
**Xưởng Dệt Ti Biển** là khu vực lao động chính, gồm hai mươi khung cửi thô sơ bằng xương cá và san hô chết, nơi năm mươi Thợ Dệt làm việc suốt ngày đêm luân phiên hai ca — tiếng khung cửi kẽo kẹt không bao giờ ngừng là âm thanh đặc trưng của khu bần dân, vọng ra xa đến nỗi Lệ Vệ canh gác cũng dùng nó để xác nhận bần dân vẫn đang lao động; nếu tiếng cửi ngừng quá nửa khắc, Lệ Vệ sẽ đến kiểm tra ngay. **Nhà Ở Xương Cá** là các túp lều chật chội, không có hệ thống sưởi ấm hay chiếu sáng, chỉ dựa vào ánh sáng lờ mờ từ rêu phát quang mà trẻ con cạo từ vách đá về dán lên tường — tạo ra thứ ánh sáng xanh nhạt u ám mà bần dân gọi là "Ánh Đêm." **Bệ Tập Kết** nằm ở lối vào duy nhất của khu bần dân, là khu vực hoàng tộc đến thu gom ti biển và ngọc trai mỗi tuần vào ngày Hải Triều — cũng là nơi phát lương thực, và là nơi duy nhất bần dân được nhìn thấy ánh sáng từ bên ngoài. **Hốc Đá Lệ Vân** ẩn dưới nền Xưởng Dệt, là nơi lão bí mật tu luyện và cất giấu mảnh sách Thủy Lưu Thuật cùng bản đồ tuyến đường di tản.

## VIII. Kinh Tế (经济)
Kinh tế khu bần dân hoàn toàn phụ thuộc vào hoàng tộc theo mô hình bóc lột triệt để. Bần dân sản xuất ti biển và ngọc trai nước mắt, toàn bộ sản phẩm bị hoàng tộc thu hết không trả thù lao, chỉ phát lại lương thực ở mức tối thiểu đủ để duy trì sức lao động — mỗi lần phát lương thực, Giám Công hoàng tộc tên Ngọc Lãnh còn đích thân đếm từng con cá muối, không bao giờ thừa một con. Bần dân không có quyền sở hữu tài sản, không được phép trao đổi hàng hóa với bên ngoài, và bị cấm rời khu vực mà không có giấy phép từ hoàng tộc — giấy phép này trong lịch sử chưa từng được cấp cho bất kỳ bần dân nào. Đây là hệ thống nô lệ trá hình dưới lớp vỏ "phân công xã hội truyền thống", và là nguồn cơn cho mọi mâu thuẫn âm ỉ trong lòng xã hội Giao Nhân Tộc. Một số học giả Giao Nhân Tộc Liên Minh ước tính tổng giá trị sản phẩm bần dân tạo ra mỗi năm lên đến hai vạn linh thạch hạ phẩm — số tiền đủ để nuôi sống họ trong sung túc, nhưng thay vào đó họ chỉ nhận lại tảo khô và cá muối.

## IX. Lịch Sử Tóm Tắt (简史)
Giai cấp bần dân đã tồn tại song song với Giao Nhân hoàng tộc từ thuở sơ khai, hình thành từ sự phân hóa quyền lực trong nội bộ chủng tộc khi một nhánh Giao Nhân khai mở được huyết mạch thượng cổ và tự xưng là dòng dõi "Chân Lệ" — nước mắt trong suốt — còn phần còn lại bị đẩy xuống thành "Trọc Lệ" — nước mắt đục. Suốt hàng ngàn năm, bần dân cam chịu kiếp nô lệ, cho đến khi hai trăm năm trước, một cuộc nổi dậy bùng phát dưới sự lãnh đạo của Lệ Huyết — tổ tiên bảy đời của Lệ Vân. Cuộc khởi nghĩa bùng nổ vào đêm Hải Triều Huyết — đêm trăng đỏ — khi bần dân đồng loạt phá cửi và tấn công Lệ Vệ bằng xương cá mài nhọn, giết được mười ba vệ binh trước khi hoàng tộc điều Kim Đan trưởng lão đến đàn áp. Hàng trăm bần dân bị giết, Lệ Huyết bị xử trảm công khai tại Bệ Tập Kết — cùng một nơi phát lương thực — và những quy định kiểm soát càng trở nên nghiệt ngã hơn: cấm tụ tập quá năm người, cấm sở hữu vật nhọn, cấm hát to. Lệ Vân, hậu duệ trực hệ, được chỉ định làm Trưởng Khu vì hoàng tộc cho rằng gia tộc này đã bị bẻ gãy ý chí. Họ không biết rằng lão đang âm thầm kết nối với Giao Nhân Tộc Liên Minh bên ngoài thông qua sứa truyền tin, chờ đợi thời cơ cho một cuộc giải phóng thực sự — lần này không phải nổi dậy, mà là di tản toàn bộ hai trăm người ra khỏi Lệ Oa.

## X. Giai Thoại & Bí Mật (轶事与秘密)
Bí mật lớn nhất khu bần dân là sự tồn tại của một bé gái Giao Nhân tên Tiểu Mặc có nước mắt hóa thành hắc ngọc trai — loại ngọc trai đen tuyền cực kỳ hiếm có, là vật cấm kỵ trong truyền thuyết Giao Nhân, tương truyền có khả năng hấp thu và phong ấn linh lực. Trong truyền thuyết, viên hắc ngọc trai cuối cùng xuất hiện cách đây ba nghìn năm, thuộc về Giao Nhân Thủy Tổ, và từng được dùng để phong ấn một hải thú thượng cổ. Nếu hoàng tộc phát hiện, họ sẽ không ngần ngại giết cả khu bần dân để đoạt lấy cô bé. Lệ Vân đang che giấu Tiểu Mặc bằng mọi giá, nhờ bà Mẫu Châu và ba Giao Nhân già đáng tin cậy nhất chăm sóc cô bé trong một hốc đá biệt lập ở góc xa nhất khu bần dân, đảm bảo cô bé không bao giờ khóc trước mặt người lạ — mỗi khi Giám Công Ngọc Lãnh đến thu ngọc trai, Tiểu Mặc được giấu trong bóng tối với miệng ngậm rong biển khô. Ngoài ra, Lệ Vân đã bí mật thiết lập được đường dây liên lạc với Giao Nhân Tộc Liên Minh bên ngoài thông qua những con sứa truyền tin gắn mảnh ti biển mã hóa, lên kế hoạch cho một cuộc di tản quy mô lớn qua tuyến hải lưu lạnh mà Lệ Vệ không tuần tra — kế hoạch mang mật danh "Đêm Trọc Lệ," dự kiến thực hiện vào mùa bão tiếp theo khi Lệ Vệ rút về tránh bão.

## XI. Quan Hệ Thế Lực (势力关系)
- **Giao Nhân Hoàng Tộc:** Kẻ áp bức trực tiếp, kiểm soát toàn diện đời sống bần dân từ lao động đến sinh sản — mỗi năm hoàng tộc chỉ cho phép ba cặp bần dân sinh con, nhằm kiểm soát dân số ở mức "vừa đủ lao động." Bần dân căm ghét nhưng không dám phản kháng công khai, bài học đẫm máu từ cuộc nổi dậy của Lệ Huyết vẫn còn khắc sâu — vết chém trên Bệ Tập Kết nơi Lệ Huyết bị xử trảm vẫn chưa ai dám lấp.
- **Giao Nhân Tộc Liên Minh:** Hy vọng duy nhất của bần dân, Lệ Vân bí mật liên lạc để tìm kiếm sự hỗ trợ giải phóng. Tuy nhiên, liên minh cũng có mục đích riêng — họ muốn Tiểu Mặc và hắc ngọc trai làm vũ khí chính trị — và bần dân không chắc có thể hoàn toàn tin tưởng. Lệ Vân biết rõ điều này nhưng không có lựa chọn khác: "Kẻ chết đuối không kén phao."
- **Ngọc Trai Sâu Phường:** Phường thu mua ngọc trai gián tiếp hưởng lợi từ sức lao động bần dân, bần dân ghét nhưng không có khả năng đối đầu. Trưởng phường Ngọc Triều từng nói: "Ngọc trai xám cũng là ngọc trai" — câu nói vô tình thừa nhận giá trị của thứ mà hoàng tộc coi là thấp kém.