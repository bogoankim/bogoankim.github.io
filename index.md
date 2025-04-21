---
layout: single
classes: wide
author_profile: true
---

<style>
  /* 전체 기본 텍스트 설정 */
  .page-content {
    font-size: 12px;
    line-height: 1.5;
  }

  /* Biography 위 여백 제거 */
  .page-content > .section:first-of-type {
    margin-top: 0 !important;
    padding-top: 0 !important;
  }

  /* 섹션 간 여백 최소화 */
  .section {
    scroll-margin-top: 10px;
    padding-top: 4px;
    padding-bottom: 4px;
    margin-top: 0.3em;      /* 섹션 간 간격 더 줄임 */
    margin-bottom: 0.3em;
}


  /* 섹션 제목 스타일 */
  .section-title {
    font-size: 1.25rem;
    font-weight: 700;  /* 적당한 bold 느낌 (기존보다 덜 두꺼움) */
    margin-bottom: 0.25em;
    margin-top: 0em;   /* 위쪽 여백 방지 */
    color: #000;       /* 확실히 검정색으로 강조 */
}


  /* 섹션 제목 아래 구분선: 연한 회색 + 얇음 */
  hr.sep {
    border: none;
    border-top: 1px solid #ccc;
    margin: 0.3em 0 0.4em 0;
  }

  /* 본문 글자 크기 */
  .section p,
  .section li,
  .section td,
  .section .inner-li,
  .section .paper_content {
    font-size: 0.85em;
  }

  /* 리스트 들여쓰기 */
  .my_list {
    list-style-type: disc;
    padding-left: 1.25em;
    margin-top: 0.25em;
  }

  .my_list .inner-ul {
    list-style-type: circle;
    padding-left: 1.5em;
    margin-top: 0.2em;
  }

  .inner-li {
    font-style: italic;
  }

  .dot-sep::before {
    content: " • ";
    padding: 0 0.25em;
  }

  /* 논문 정보 테이블 */
  table.my_list {
    width: 100%;
    font-size: 0.95em;
    border-collapse: collapse;
  }

  table.my_list tr {
    border: none !important;
  }

  table.my_list td {
    vertical-align: top;
    padding-bottom: 0.75em;
    border-bottom: none !important;
  }

  /* [C13] 같은 문헌 코드 스타일 */
  .paper_head {
    vertical-align: top;
    padding-right: 0.2em;
    font-weight: bold;
    white-space: nowrap;
    width: 3.5%;
    text-align: right;
  }

  .paper_content {
    padding-top: 0.6em;
    padding-bottom: 0.4em;
    border-bottom: none;
  }

  /* 좌측 이름 텍스트 크기 축소 + 검정 */
  .author__name {
    font-size: 1.0rem !important;
    font-weight: 700 !important;
    color: #000 !important;
  }

  /* 좌측 이미지: 라운드 사각형 */
  .author__avatar img {
    border-radius: 12px !important;
    object-fit: cover;
  }

  /* 📱 모바일에서 좌측 프로필 여백 및 폰트 조정 */
  @media only screen and (max-width: 768px) {
  .author__avatar {
    margin-bottom: 0.5rem !important; /* 이미지 아래 간격 줄임 */
  }

  .author__name {
    margin-bottom: 0.25rem !important; /* 이름과 직책 사이 간격 줄임 */
    font-size: 0.95rem !important;     /* 모바일에서 살짝 더 작게 */
  }

  .author__bio {
    margin-bottom: 0.25rem !important; /* 직책 아래 간격 줄임 */
  }
}

  .venue.conf strong {
    color: #9b0000; /* 붉은색: 학회 */
}

  .venue.journal strong {
    color: #0056d2; /* 고동색: 저널 */
}

a {
  color: #4285f4;
}

</style>

<div id="bio" class="section">
	<h5 class="section-title">Biography</h5>
	<hr class="sep">
	<p> Bogoan Kim is a postdoctoral researcher at <a href="https://www.kaist.ac.kr/web/eng">KAIST</a>, supported by the Jang Young Sil Fellow Program and working under the supervision of <a href="https://dxd-lab.github.io/">Prof. Hwajung Hong</a> and <a href="https://scholar.google.co.kr/citations?user=Sc2pBzYAAAAJ&hl=en">Prof. Uichin Lee</a>. He received his Ph.D. in Artificial Intelligence from <a href="https://www.hanyang.ac.kr">Hanyang University</a>, where he was supported by the NRF of Korea Ph.D. Fellowship and advised by <a href="http://hcc.hanyang.ac.kr/">Prof. Kyungsik Han</a>. His research lies at the intersection of Human–Computer Interaction and digital health, focusing on the design and development of data-driven interventions to promote well-being. Leveraging mobile and virtual reality technologies, his work aims to provide holistic support for mental and behavioral health. He takes a user-centered and adaptive approach to system design, with particular emphasis on evidence-based digital transformation that addresses the diverse needs of socio-technical ecosystems.
	</p>
</div>


<div id="exp" class="section">
	<h5 class="section-title">Positions</h5>
	<hr class="sep">
	<ul class="my_list">
		<li><strong class="title">KAIST</strong>, Daejeon, Korea  <span class="dot-sep"></span> May 2025 - Present
			<ul class="inner-ul">
				<li class="inner-li"> <i>Postdoctoral Researcher, College of Engineering</i> 
					(Advisors: <a href="https://dxd-lab.github.io/">Prof. Hwajung Hong</a> and <a href="https://scholar.google.co.kr/citations?user=Sc2pBzYAAAAJ&hl=en">Prof. Uichin Lee</a>) </li>
			</ul>
		</li>  
		<li><strong class="title">Hanyang University</strong>, Seoul, Korea  <span class="dot-sep"></span> Mar 2025 - Apr. 2025 
			<ul class="inner-ul">
				<li class="inner-li"> <i>Postdoctoral Researcher, Department of Data Science</i> 
					(Advisor: <a href="http://hcc.hanyang.ac.kr/">Prof. Kyungsik Han</a>) </li>
			</ul>
		</li>
		<li><strong class="title">The Pennsylvania State University</strong>, PA, USA <span class="dot-sep"></span> Jan 2020 - Jun 2020
			<ul class="inner-ul">
				<li class="inner-li"> <i>Visiting Scholar, College of Information Sciences and Technology (IST)</i> 
					(Advisors: <a href="https://pike.psu.edu/dongwon/">Prof. Dongwon Lee</a> and <a href="https://faculty.ist.psu.edu/axx29/">Prof. Aiping Xiong</a></li>
			</ul>
		</li>
		<li><strong class="title">Indiana University - Bloomington</strong>, IN, USA <span class="dot-sep"></span> Oct. 2019 - Feb. 2020 
			<ul class="inner-ul">
				<li class="inner-li"> <i>Visiting Scholar, Luddy School of Informatics</i> 
					(Advisors: <a href="https://patshih.luddy.indiana.edu/">Prof. Patich C. Shih</a> and <a href="https://publichealth.indiana.edu/research/faculty-directory/profile.html?user=gfrey">Prof. Georgia C.Frey</a>) </li>
			</ul>
		</li>
	</ul>
</div>

<div id="edu" class="section">
	<h5 class="section-title">Education</h5>
	<hr class="sep">
	<ul class="my_list">
		<li><strong class="title">Hanyang University</strong>, Seoul, Korea <span class="dot-sep"></span> Aug. 2021
			<ul class="inner-ul">
				<li class="inner-li"> <i>Ph.D in Artificial Intelligence</i> 
					(Advisor: <a href="http://hcc.hanyang.ac.kr/">Kyungsik Han</a>)  </li>
				<li class="inner-li"> Dissertation: BalancePath: AI-VR Framework for Personalized Adaptive System </li>
			</ul>
		</li>
		<li><strong class="title"> University of Minnesota - Twin Cities</strong>, MN, USA <span class="dot-sep"></span> Aug. 2013 <br>
			<ul class="inner-ul">
				<li class="inner-li"> <i>B.A in Statistics </i></li>
			</ul>
		</li>
	</ul>
</div>


<div id="pub" class="section">
<h5 class="section-title">Publications <small>(* indicates equal contributions)</small></h5>
<hr class="sep">
	<!-- <span class="year"><strong>Preprints</strong></span> -->
	<!-- <span class="year"><strong>2024 and Forthcoming</strong></span> -->
	<table class="my_list">
		<tr>
			<td class="paper_head"> <strong>[P13]</strong></td>
			<td class="paper_content">
			<strong class='title'>"I Don’t Know Why I Should Use This App”: Holistic Analysis on User Engagement Challenges in Mobile Mental Health</strong>
			<br> 
			{Seungwan Jin*, <strong><u>Bogoan Kim*</u></strong>}, and Kyungsik Han <br> 
			<span class="venue conf"><strong>ACM CHI 2025</strong></span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[P12]</strong></td>
			<td class="paper_content">
			<strong class='title'>Narrating Routines through Game Dynamics: Impact of a Gamified Routine Management App for Autistic Individuals</strong> <br> 
			<strong><u>Bogoan Kim</u></strong>, Dayoung Jeong, Hwajung Hong and Kyungsik Han <br> 
			<span class="venue conf"><strong>ACM CHI 2024</strong></span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[P11]</strong></td>
			<td class="paper_content">
			<strong class='title'>Promoting Self-Efficacy of Individuals With Autism in Practicing Social Skills in the Workplace Using Virtual Reality and Physiological Sensors: Mixed Methods Study</strong> <br> 
			Sung-In Kim, So-youn Jang, Taewan Kim, <strong><u>Bogoan Kim</u></strong>, Dayoung Jeong, Taehyung Noh, Mingon Jeong, Kaely Hall, Meelim Kim, Hee Jeong Yoo, Kyungsik Han, Hwajung Hong and Jennifer G Kim <br> 
			<span class="venue journal"> <strong>JMIR Formative Research</strong> (SCIE, 2024)</span> 
			</td>
		</tr>
		<tr class="paper" style="border-bottom: 0px;">
			<td class="paper_head"> <strong>[P10]</strong></td>
			<td class="paper_content">
				<strong class='title'>V-DAT: Supporting Self-Awareness for Autistic People from Multimodal VR Sensor Data</strong> <br> 
				<strong><u>Bogoan Kim</u></strong>, Dayoung Jeong, Jennifer G Kim, Hwajung Hong, and Kyungsik Han <br> 
				<span class="venue conf"><strong>ACM UIST 2023</strong></span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[P9]</strong></td>
			<td class="paper_content">
			<strong class='title'>RoutineAid: Externalizing Key Design Elements to Support Daily Routines of Individuals with Autis</strong> <br> 
			<strong><u>Bogoan Kim</u></strong>, Sung-In Kim, Sungwon Park, Hee Jeong Yoo, Hwajung Hong, and Kyungsik Han <br> 
			<span class="venue conf"><strong>ACM CHI 2023</strong></span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[P8]</strong></td>
			<td class="paper_content">
			<strong class='title'>VISTA: User-Centered VR Training System for Effectively Deriving Characteristics of Autistic Individuals</strong> <br>  
			<strong><u>Bogoan Kim</u></strong>, Dayoung Jeong, Mingon Jeong, Taehyoung Noh, Sung-In Kim, Taewan Kim, So-youn Jang, Hee Jeong Yoo, Jennifer G Kim, Hwajung Hong, and Kyungsik Han <br>
			<span class="venue conf"><strong>ACM VRST 2022</strong></span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[P7]</strong></td>
			<td class="paper_content">
			<strong class='title'>A Systematic Review on Fake News Research through the Lens of News Creation and Consumption: Research Efforts, Challenges, and Future Direction</strong> <br> 
			<strong><u>Bogoan Kim</u></strong>, Aiping Xiong, Dongwon Lee, and Kyungsik Han <br> 
			<span class="venue journal"> <strong>PLoS ONE</strong> (SCIE, 2021)</span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[P6]</strong></td>
			<td class="paper_content">
			<strong class='title'>ChamberBreaker: Mitigating the Echo Chamber Effect and Supporting Information Hygiene through a Gamified Inoculation 				System</strong> <br> 
			Youngseung Jeon, <strong><u>Bogoan Kim</u></strong>, Aiping Xiong, Dongwon Lee, and Kyungsik Han <br> 
			<span class="venue conf"><strong>ACM CSCW 2021</strong></span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[P5]</strong></td>
			<td class="paper_content">
			<strong class='title'>Usability Assessment of a Mobile Health Intervention for Increasing Physical Activity in Autistic Adults</strong> <br> 
			Daehyoung Lee, Georgia C Frey, Aehong Min, <strong><u>Bogoan Kim</u></strong>, Donneta J Cothran, Scott Bellini, Kyungsik Han, and Patrich C 				Shih<br> 
			<span class="venue journal"> <strong>Health Informatics Journal</strong> (SCIE, 2020)</span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[P4]</strong></td>
			<td class="paper_content">
			<strong class='title'>PuzzleWalk: A Theory-Driven Iterative Design Inquiry of a Mobile Game for Promoting Physical Activity in Autistic 				Adults</strong> <br> 
			<strong><u>Bogoan Kim</u></strong>, Daehyoung Lee, Aehong Min, Seungwon Paik, Georgia C Frey, Scott Bellini, Kyungsik Han and Patrick C Shih <br> 
			<span class="venue journal"> <strong>PLoS ONE</strong> (SCIE, 2020)</span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[P3]</strong></td>
			<td class="paper_content">
			<strong class='title'>No More One Liners: Bringing Context into Emoji Recommendation </strong> <br> 
			Joongyum Kim, Taesik Gong, <strong><u>Bogoan Kim</u></strong>, Jaeyeon Park, Woojeong Kim, Evey Huang, Kyungsik Han, Juho Kim, Jeonggil Ko, 
			and Sung-Ju Lee <br> 
			<span class="venue journal"> <strong>ACM Transactions on Social Computing</strong> (2020)</span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[P2]</strong></td>
			<td class="paper_content">
			<strong class='title'>TM: The Effectiveness of Self-Regulation on Time Management through a Smartphone Application</strong> <br> 
			<strong><u>Bogoan Kim</u></strong>, Seok-Won Lee, Hwajung Hong, and Kyungsik Han <br> 
			<span class="venue journal"> <strong>IEEE Access</strong> (SCIE, 2019)</span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[P1]</strong></td>
			<td class="paper_content">
			<strong class='title'>Photos Don’t Have Me, But How Do You Know Me?: Analyzing and Predicting Users on Instagra</strong> <br> 
			Kyungsik Han, Youngseung Jeon, <strong><u>Bogoan Kim</u></strong>, Junho Song, and Sang-Wook Kim <br> 
			<span class="venue conf"><strong>ACM UMAP 2018</strong></span>
			</td>
		</tr>
    </table>
</div>

<div id="honors" class="section">
    <h5 class="section-title">Honors & Awards</h5>
    <hr class="sep">
	<ul class="my_list">
		<li> <strong class="title">Jang Young Sil Postdoctoral Fellowship</strong> <br>
			Ministry of Science and ICT, Korea<span class="dot-sep"></span> 2025
		</li>
		<li> <strong class="title">Hanyang University Postdoctoral Fellowship</strong> <br>
			Research Institute of Industrial Science, Hanyang University<span class="dot-sep"></span> 2025
		</li>
		<li> <strong class="title">NRF of Korea Ph.D. Fellowship</strong> <br>
			National Research Foundation of Korea<span class="dot-sep"></span> 2023
		</li>
		<li> <strong class="title">UIST Travel Grant</strong> <br>
			ACM Symposium on User Interface Software and Technology <span class="dot-sep"></span> 2023
		</li>
		<!--<li> <strong class="title">Gary Marsden Travel Award</strong> <br>
			AACM Conference on Human Factors in Computing Systems <span class="dot-sep"></span> 2023
		</li>
		<li><strong class="title">Naver Ph.D. Fellowship</strong> <br>
			Naver Corporation <span class="dot-sep"></span> 2017
		</li>
		<!-- <li> <strong class="title">Best Paper Award</strong> <br> -->
			<!-- Korea Information Processing Society (KIPS) <span class="dot-sep"></span> 2021  -->
		<!-- </li> -->
		<!-- <li><strong class="title">Best Presentation Award</strong> <br> -->
			<!-- Korea Computer Congress (KCC) <span class="dot-sep"></span> 2017 -->
		<!-- </li> -->
	</ul>
</div>
<!--
<div id="services" class="section">
    <h5 class="section-title">Professional Services</h5>
    <hr class="sep">
	<ul class="my_list">
		<li> <strong class="title">Track Co-Chair</strong> <br>
			ACM Symposium on Applied Computing (<strong>ACM SAC</strong>)<span class="dot-sep"></span> 2023 - 2025
		</li>
		<li> <strong class="title">Conference Reviewer</strong> <br>
			The ACM Web Conference (<strong>WWW</strong>) <span class="dot-sep"></span> 2023 - 2025 <br>
			The ACM SIGKDD Conference on Knowledge Discovery and Data Mining (<strong>ACM KDD</strong>) <span class="dot-sep"></span> 2021, 2022, 2024, 2025 <br>
			The IEEE International Conference on Data Mining (<strong>IEEE ICDM</strong>) <span class="dot-sep"></span> 2022, 2023 <br>
			The IEEE International Conference on Big Data (<strong>IEEE BigData</strong>), GTA3 Workshop <span class="dot-sep"></span> 2023 <br>
			The AAAI International Conference on Artificial Intelligence (<strong>AAAI</strong>) <span class="dot-sep"></span> 2021 <br>
			The ACM Symposium on Applied Computing (<strong>ACM SAC</strong>) <span class="dot-sep"></span> 2022, 2023 <br>
		</li>
		<li> <strong class="title">Journal Reviewer</strong> <br>
			The ACM Computing Surverys (<strong>ACM CSUR</strong>) <span class="dot-sep"></span> 2024 <br>
			The IEEE Transactions on Neural Networks and Learning Systems (<strong>IEEE TNNLS</strong>) <span class="dot-sep"></span> 2023 <br>
			Journal of Supercomputing <span class="dot-sep"></span> 2023 <br>
		</li>
	</ul>
</div>
-->
