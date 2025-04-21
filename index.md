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

  .venue.conf strong {
    color: #e53935; /* 붉은색: 학회 */
}

  .venue.journal strong {
    color: #6D4C41; /* 고동색: 저널 */
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
			<span class="venue conf"><strong>CHI 2025</strong></span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[P12]</strong></td>
			<td class="paper_content">
			<strong class='title'>Narrating Routines through Game Dynamics: Impact of a Gamified Routine Management App for Autistic Individuals</strong> <br> 
			<strong><u>Bogoan Kim</u></strong>, Dayoung Jeong, Hwajung Hong and Kyungsik Han <br> 
			<span class="venue conf"><strong>CHI 2024</strong></span>
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
				<strong class='title'>-DAT: Supporting Self-Awareness for Autistic People from Multimodal VR Sensor Data</strong> <br> 
				<strong><u>Bogoan Kim</u></strong>, Dayoung Jeong, Jennifer G Kim, Hwajung Hong, and Kyungsik Han <br> 
				<span class="venue conf"><strong>UIST 2023</strong></span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[P9]</strong></td>
			<td class="paper_content">
			<strong class='title'>RoutineAid: Externalizing Key Design Elements to Support Daily Routines of Individuals with Autis</strong> <br> 
			<strong><u>Bogoan Kim</u></strong>, Sung-In Kim, Sungwon Park, Hee Jeong Yoo, Hwajung Hong, and Kyungsik Han <br> 
			<span class="venue conf"><strong>CHI 2023</strong></span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[P8]</strong></td>
			<td class="paper_content">
			<strong class='title'>VISTA: User-Centered VR Training System for Effectively Deriving Characteristics of Autistic Individuals</strong> <br>  
			<strong><u>Bogoan Kim</u></strong>, Dayoung Jeong, Mingon Jeong, Taehyoung Noh, Sung-In Kim, Taewan Kim, So-youn Jang, Hee Jeong Yoo, Jennifer G Kim, Hwajung Hong, and Kyungsik Han <br>
			<span class="venue conf"><strong>VRST 2022</strong></span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[C8]</strong></td>
			<td class="paper_content">
			<strong class='title'>RealGraph<sup>GPU</sup>: A High-Performance GPU-Based Graph Engine toward Large-Scale Real-World Network Analysis</strong> <br> 
			Myung-Hwan Jang, <strong><u>Yunyong Ko</u></strong>, Dongkyu Jeong, Jeong-Min Park, and Sang-Wook Kim <br> 
			<!-- <span class="venue conf"><strong>ACM CIKM 2022</strong> (Short Paper)</span> -->
			<span class="venue conf"><strong>ACM CIKM 2022</strong> (Short Paper)</span>
			<span class="dot-sep"></span> 
			<span>[ <a href="/assets/files/CIKM22-realgraph-paper.pdf">Paper</a> | <a href="/assets/files/CIKM22-realgraph-poster.pdf">Poster</a> ]</span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[C7]</strong></td>
			<td class="paper_content">
			<strong class='title'>Not All Layers Are Equal: A Layer-Wise Adaptive Approach Toward Large-Scale DNN Training </strong> <br> 
			<strong><u>Yunyong Ko</u></strong>, Dongwon Lee, and Sang-Wook Kim <br> 
			<!-- <span class="venue conf">ACM Web Conference (<strong>WWW</strong>) 2022</span> -->
			<span class="venue conf"><strong>WWW 2022</strong></span>
			<span class="dot-sep"></span> 
			<span>[ <a href="/assets/files/WWW22-lena-paper.pdf">Paper</a> | <a href="https://github.com/yy-ko/lena-www22">Code</a> | <a href="/assets/files/WWW22-lena-presentation.pdf">Slides</a> ]</span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[C6]</strong></td>
			<td class="paper_content">
			<strong class='title'>D-FEND: A Diffusion-Based Fake News Detection Framework for News Articles Related to COVID-19</strong> <br> 
			Soeun Han, <strong><u>Yunyong Ko</u></strong>, Yusim Kim, Heejin Park, Seongsu Oh, and Sang-Wook Kim<br> 
			<span class="venue conf"><strong>ACM SAC 2022</strong></span>
			<span class="dot-sep"></span> 
			<span>[ <a href="/assets/files/SAC22-dfend-paper.pdf">Paper</a> | <a href="/assets/files/SAC22-dfend-presentation.pdf">Slides</a> ]</span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[C5]</strong></td>
			<td class="paper_content">
			<strong class='title'>MASCOT: A Quantization Framework for Efficient Matrix Factorization in Recommender Systems </strong> <br> 
			{<strong><u>Yunyong Ko*</u></strong>, Jae-Su Yu*}, Hong-Kyun Bae, Yongjun Park, Dongwon Lee, and Sang-Wook Kim <br> 
			<!-- <span class="venue conf">IEEE International Conference on Data Mining (<strong>IEEE ICDM</strong>) 2021</span> -->
			<span class="venue conf"><strong>IEEE ICDM 2021</strong></span>
			<span class="dot-sep"></span> 
			<span>[ <a href="/assets/files/ICDM21-mascot-paper.pdf">Paper</a> <span> | </span> <a href="https://github.com/yy-ko/mascot-icdm21">Code</a> <span>|</span> <a href="/assets/files/ICDM21-mascot-presentation.pdf">Slides</a> ]</span> <br>
			<span class="award">Selected as One of the Best-ranked Papers of ICDM 2021 for fast-track journal invitation</span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[C4]</strong></td>
			<td class="paper_content">
			<strong class='title'>ALADDIN: Asymmetric Centralized Training for Distributed Deep Learning </strong> <br> 
			<strong><u>Yunyong Ko</u></strong>, Kibong Choi, Hyunseung Jei, Dongwon Lee, and Sang-Wook Kim <br> 
			<!-- <span class="venue conf">ACM International Conference on Information and Knowledge Management (<strong>ACM CIKM</strong>) 2021</span>  -->
			<span class="venue conf"><strong>ACM CIKM 2021</strong></span>
			<span class="dot-sep"></span>
			<span>[ <a href="/assets/files/CIKM21-aladdin-paper.pdf">Paper</a> <span>|</span> <a href="/assets/files/CIKM21-aladdin-poster.pdf">Poster</a> <span>|</span> <a href="/assets/files/CIKM21-aladdin-presentation.pdf">Slides</a> <span>|</span> <a href="https://sites.google.com/view/aladdin-proofs/home?authuser=0">Appendix</a> ]</span> <br>
			<span class="award">Selected as a Spotlight Presentation of CIKM 2021 </span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[C3]</strong></td>
			<td class="paper_content">
			<strong class='title'>An In-Depth Analysis on Distributed Training of Deep Neural Networks </strong> <br> 
			<strong><u>Yunyong Ko</u></strong>, Kibong Choi, Jiwon Seo, and Sang-Wook Kim <br> 
			<!-- <span class="venue conf">IEEE International Parallel and Distributed Processing Symposium (<strong>IEEE IPDPS</strong>) 2021</span> -->
			<span class="venue conf"><strong>IEEE IPDPS 2021</strong></span>
			<span class="dot-sep"></span>
			<span>[ <a href="/assets/files/IPDPS21-analysis-paper.pdf">Paper</a> <span>|</span> <a href="/assets/files/IPDPS21-analysis-presentation.pdf">Slides</a> ]</span> <br>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[C2]</strong></td>
			<td class="paper_content">
			<strong class='title'>Influence Maximization for Effective Advertisement in Social Networks: Problem, Solution, and Evaluation</strong> <br> 
			Suk-Jin Hong, <strong><u>Yunyong Ko</u></strong>, Moon-Jeung Joe, and Sang-Wook Kim <br> 
			<span class="venue conf"><strong>ACM SAC 2019</strong></span>
			<span class="dot-sep"></span> 
			<span>[ <a href="/assets/files/SAC19-infmax-paper.pdf">Paper</a> ]</span>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[J2]</strong></td>
			<td class="paper_content">
			<strong class='title'>Efficient and Effective Influence Maximization in Social Networks: A Hybrid-Approach </strong> <br> 
			<strong><u>Yunyong Ko</u></strong>, Kyung-Jae Cho, and Sang-Wook Kim <br> 
			<span class="venue journal"> <strong>Information Sciences</strong> (SCIE, 2018)</span> 
			<span class="dot-sep"></span> 
			<span>[ <a href="/assets/files/INS18-hybrid-paper.pdf">Paper</a> ]</span> <br>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[J1]</strong></td>
			<td class="paper_content">
			<strong class='title'>Influence Maximization in Social Networks: A Target-Oriented Estimation</strong> <br> 
			<strong><u>Yunyong Ko</u></strong>, Dong-Kyu Chae, and Sang-Wook Kim <br> 
			<span class="venue journal"> <strong>Journal of Information Science</strong> (SCIE, 2018)</span> 
			<span class="dot-sep"></span> 
			<span>[ <a href="/assets/files/JIS18-target-paper.pdf">Paper</a> ]</span> <br>
			</td>
		</tr>
		<tr>
			<td class="paper_head"> <strong>[C1]</strong></td>
			<td class="paper_content">
			<strong class='title'>Accurate Path-Based Influence Maximization in Social Networks </strong> <br> 
			<strong><u>Yunyong Ko</u></strong>, Dong-Kyu Chae, and Sang-Wook Kim <br> 
			<!-- <span class="venue conf"><strong>WWW 2016</strong> (Short Paper)</span> -->
			<span class="venue conf"><strong>WWW 2016</strong> (Short Paper)</span>
			<span class="dot-sep"></span> 
			<span>[ <a href="/assets/files/WWW16-path-paper.pdf">Paper</a> ]</span> <br>
			</td>
		</tr>
    </table>
</div>

<div id="honors" class="section">
    <h5 class="section-title">Honors & Awards</h5>
    <hr class="sep">
	<ul class="my_list">
		<li> <strong class="title">Scholarship and Teaching for Engineering Postdocs (STEP)</strong> <br>
			Grainger College of Engineering (GCOE), University of Illinois at Urbana-Champaign<span class="dot-sep"></span> 2023
		</li>
		<li> <strong class="title">Best Ranked Papers of IEEE ICDM</strong> <br>
			IEEE International Conference on Data Mining<span class="dot-sep"></span> 2021
		</li>
		<li> <strong class="title">Spotlight Presentations of ACM CIKM</strong> <br>
			ACM International Conference on Information and Knowledge Management<span class="dot-sep"></span> 2021
		</li>
		<li> <strong class="title">Outstanding Ph.D. Dissertation Award</strong> <br>
			Research Institute of Industrial Science, Hanyang University <span class="dot-sep"></span> 2021
		</li>
		<li> <strong class="title">ACM SIGAPP Student Travel Award</strong> <br>
			ACM Symposium on Applied Computing <span class="dot-sep"></span> 2019
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
