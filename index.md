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
    font-style: normal;
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

  @media only screen and (max-width: 768px) {
  .author__avatar {
    margin-bottom: 0.15rem !important; /* 이미지 아래 간격 더 줄임 */
  }

  .author__content {
    margin-top: 0 !important; /* 이름과 직함 부분과 그 아래 텍스트 간격 제거 */
  }

  .author__name {
    font-size: 0.95rem !important; /* 이름 글씨 약간 작게 */
    margin-bottom: 0.1rem !important; /* 이름과 직책 사이 간격 축소 */
  }

  .author__bio {
    font-size: 0.85rem !important;  /* 직책 크기도 조금 줄임 */
    margin-bottom: 0.2rem !important; /* 직책과 내용 사이 간격도 축소 */
  }
}

@media only screen and (max-width: 768px) {
  #bio {
    margin-top: 0.5rem !important;  /* 여백 줄이기 */
    padding-top: 0.3rem !important;
  }

  .section {
    margin-top: 0.75rem !important;  /* 전체 섹션 간 여백도 축소 */
    margin-bottom: 0.75rem !important;
  }
}

.venue.conf {
  color: #2D7F7A;
}

.venue.journal {
  color: #A12A2A;
}

.venue-note {
  font-size: 0.9em;
}

a {
  color: #4285f4;
}
/* 새로 추가 */
.my_list {
list-style: none;
padding-left: 0;
margin-left: 0;
}

.my_list .pub-item {
display: flex;
align-items: flex-start;
gap: 14px;
margin-bottom: 1.1em;
}

.my_list .pub-num {
width: 54px;
min-width: 54px;
flex: 0 0 54px;
font-weight: 700;
line-height: 1.35;
}

.my_list .pub-body {
flex: 1;
min-width: 0;
line-height: 1.35;
}

.my_list .pub-award {
display: flex;
align-items: center;
justify-content: flex-start;
gap: 5px;
color: #1F5CFF;
font-size: inherit;
font-weight: 700;
margin-bottom: 2px;
line-height: 1.2;
}

.my_list .pub-award img {
height: 0.8em;
width: auto;
display: block;
flex: 0 0 auto;
}

</style>

<div id="bio" class="section">
	<h5 class="section-title">Biography</h5>
	<hr class="sep">
	<p>
  Bogoan Kim is an Assistant Professor in the
  <a href="https://inform.chungbuk.ac.kr/">School of Information and Communication Engineering, Chungbuk National University</a>,
  where he leads the <a href="https://sites.google.com/view/cbnu-hci">HCI Lab</a>.
  Prior to joining CBNU, he was a Postdoctoral Researcher at KAIST, supported by the Jang Young Sil Fellowship,
  working with Prof. Hwajung Hong and Prof. Uichin Lee.
  He earned his Ph.D. in Artificial Intelligence from Hanyang University under the supervision of Prof. Kyungsik Han,
  supported by the NRF of Korea Ph.D. Fellowship.
</p>

</div>

<div id="exp" class="section">
	<h5 class="section-title">Positions</h5>
	<hr class="sep">
	<ul class="my_list">
		<li><strong class="title">Chungbuk National University</strong>, Cheongju, Korea <span class="dot-sep"></span> Sep 2025 – Present
			<ul class="inner-ul">
				<li class="inner-li"> <i>Assistant Professor, School of Information and Communication Engineering</i> </li>
			</ul>
		</li>
		<li><strong class="title">KAIST</strong>, Daejeon, Korea  <span class="dot-sep"></span> Mar 2025 - Aug 2025
			<ul class="inner-ul">
				<li class="inner-li"> <i>Jang Young-Sil Postdoctoral Fellow, College of Engineering</i> 
					(Advisors: <a href="https://dxd-lab.github.io/">Prof. Hwajung Hong</a> and <a href="https://scholar.google.co.kr/citations?user=Sc2pBzYAAAAJ&hl=en">Prof. Uichin Lee</a>) </li>
			</ul>
		</li>
		<!-- <li><strong class="title">Hanyang University</strong>, Seoul, Korea  <span class="dot-sep"></span> Mar 2025 - April 2025 
			<ul class="inner-ul">
				<li class="inner-li"> Postdoctoral Researcher, Department of Data Science 
					(Advisor: <a href="http://hcc.hanyang.ac.kr/">Prof. Kyungsik Han</a>) </li>
			</ul>
		</li> -->
		<li><strong class="title">The Pennsylvania State University</strong>, PA, USA <span class="dot-sep"></span> Jan 2020 - Jun 2020
			<ul class="inner-ul">
				<li class="inner-li"> Visiting Researcher, College of IST 
					(Advisors: <a href="https://pike.psu.edu/dongwon/">Prof. Dongwon Lee</a> and <a href="https://faculty.ist.psu.edu/axx29/">Prof. Aiping Xiong</a>)</li>
			</ul>
		</li>
		<li><strong class="title">Indiana University - Bloomington</strong>, IN, USA <span class="dot-sep"></span> June 2019 - Sep 2019 
			<ul class="inner-ul">
				<li class="inner-li"> Visiting Researcher, Luddy School of Informatics
					(Advisors: <a href="https://patshih.luddy.indiana.edu/">Prof. Patich C. Shih</a> and <a href="https://publichealth.indiana.edu/research/faculty-directory/profile.html?user=gfrey">Prof. Georgia C.Frey</a>) </li>
			</ul>
		</li>
	</ul>
</div>

<div id="edu" class="section">
	<h5 class="section-title">Education</h5>
	<hr class="sep">
	<ul class="my_list">
		<li><strong class="title">Hanyang University</strong>, Seoul, Korea <span class="dot-sep"></span> Feb 2025
			<ul class="inner-ul">
				<li class="inner-li"> Ph.D in Artificial Intelligence
					(Advisor: <a href="http://hcc.hanyang.ac.kr/">Kyungsik Han</a>)  </li>
				<li class="inner-li"> Dissertation: BalancePath: AI-VR Framework for Personalized Adaptive System </li>
			</ul>
		</li>
		<li><strong class="title"> University of Minnesota - Twin Cities</strong>, MN, USA <span class="dot-sep"></span> Jan 2017 <br>
			<ul class="inner-ul">
				<li class="inner-li"> B.S in Statistics (Graduated with honors) </li>
			</ul>
		</li>
	</ul>
</div>

<div id="pub" class="section"> 
  <!-- <small>(For a complete list, please visit <a href="https://sites.google.com/view/cbnu-hci">our Lab Homepage</a>)</small> -->
  <h5 class="section-title">Publications </h5>
  <hr class="sep">

  <ul class="my_list">
    <li class="pub-item">
      <span class="pub-num">[27]</span>
      <div class="pub-body">
        <div class="pub-award">
          <img src="assets/images/medal.png" alt="Medal">
          <span>Best Paper Honorable Mention Award</span>
        </div>
        <strong class="title">QuerySwitch: Supporting the Design Process by Balancing Vagueness through LLMs</strong><br>
        M Kim, <strong><u>B Kim</u></strong>, and K Han<br>
        <span class="venue conf"><strong>ACM CHI 2026</strong><span class="venue-note"> | <i>ACM International Conference on Human Factors in Computing Systems</i></span></span>
      </div>
    </li>
    <li class="pub-item">
      <span class="pub-num">[26]</span>
      <div class="pub-body">
        <strong class="title">LAPS: Automating Hypothesis-Driven Statistical Analysis of Public Survey Using LLMs</strong><br>
        {J Kim*, D Jeong*}, B Son, H Kim, <strong><u>B Kim</u></strong>, and K Han<br>
        <span class="venue conf"><strong>ACM CHI 2026</strong><span class="venue-note"> | <i>ACM International Conference on Human Factors in Computing Systems</i></span></span>
      </div>
    </li>
    <li class="pub-item">
      <span class="pub-num">[25]</span>
      <div class="pub-body">
        <div class="pub-award">
          <img src="assets/images/medal.png" alt="Medal">
          <span>Best Paper Honorable Mention Award</span>
        </div>
        <strong class="title">“I Choose to Live, for Life Itself”: Understanding Agency of Home-Based Care Patients Through Information Practices and Relational Dynamics in Care Networks</strong><br>
        {S-I Kim*, J Park*}, <strong><u>B Kim</u></strong>, and H Hong<br>
        <span class="venue conf"><strong>ACM CHI 2026</strong><span class="venue-note"> | <i>ACM International Conference on Human Factors in Computing Systems</i></span></span>
      </div>
    </li>
    <li class="pub-item">
      <span class="pub-num">[24]</span>
      <div class="pub-body">
        <strong class="title">Understanding Human-Multi-Agent Team Formation for Creative Work</strong><br>
        H Lim, D Choi, S Nam, <strong><u>B Kim</u></strong>, and H Hong<br>
        <span class="venue conf"><strong>ACM CHI 2026</strong><span class="venue-note"> | <i>ACM International Conference on Human Factors in Computing Systems</i></span></span>
      </div>
    </li>
    <li class="pub-item">
      <span class="pub-num">[23]</span>
      <div class="pub-body">
        <strong class="title">VR-ACT: Transforming Clinical Evidence of Acceptance Commitment Therapy through Virtual Reality for Subthreshold Depression</strong><br>
        <strong><u>B Kim</u></strong>, D Jeong, YS Choi, H Kim, and K Han<br> 
        <span class="venue journal"><strong>Springer Virtual Reality</strong><span class="venue-note"> (SCIE, 2026.03)</span></span>
      </div>
    </li>
    <li class="pub-item">
      <span class="pub-num">[22]</span>
      <div class="pub-body">
        <strong class="title">Enhancing Mindfulness-Based Cognitive Therapy in a VR: A Prospective Interventional Study</strong><br>
        {<strong><u>B Kim*</u></strong>, D Jeong*}, YS Choi, Y Choi, H Kim, and K Han<br> 
        <span class="venue journal"><strong>Scientific Reports</strong><span class="venue-note"> (SCIE, 2025.09)</span></span>
      </div>
    </li>
    <li class="pub-item">
      <span class="pub-num">[21]</span>
      <div class="pub-body">
        <strong class="title">"I Don’t Know Why I Should Use This App”: Holistic Analysis on User Engagement Challenges in Mobile Mental Health</strong><br>
        {S Jin*, <strong><u>B Kim*</u></strong>}, and K Han<br>
        <span class="venue conf"><strong>ACM CHI 2025</strong><span class="venue-note"> | <i>ACM International Conference on Human Factors in Computing Systems</i></span></span>
      </div>
    </li>
	<li class="pub-item">
      <span class="pub-num">[20]</span>
      <div class="pub-body">
        <strong class="title">Development of a Personalized Early Prediction Model for Cybersickness in Virtual Reality</strong><br>
        YS Choi, D Jeong, B Kim, <strong><u>B Kim</u></strong>, and K Han<br>
        <span class="venue journal"><strong>KIISE Transaction on Computing Practices</strong></span>
      </div>
    </li>  
	  <li class="pub-item">
      <span class="pub-num">[19]</span>
      <div class="pub-body">
        <strong class="title">Early Prediction of Cybersickness in Virtual Reality Using a Large Language Model for Multimodal Time Series Data</strong><br>
        YS Choi, D Jeong, B Kim, <strong><u>B Kim</u></strong>, and K Han<br>
        <span class="venue conf"><strong>ACM UbiComp 2024</strong><span class="venue-note"> (Poster) | <i>ACM International Conference on Pervasive and Ubiquitous Computing</i></span></span>
      </div>
    </li>  
    <li class="pub-item">
      <span class="pub-num">[18]</span>
      <div class="pub-body">
        <strong class="title">Narrating Routines through Game Dynamics: Impact of a Gamified Routine Management App for Autistic Individuals</strong><br>
        <strong><u>B Kim</u></strong>, D Jeong, H Hong, and K Han<br>
        <span class="venue conf"><strong>ACM CHI 2024</strong><span class="venue-note"> | <i>ACM International Conference on Human Factors in Computing Systems</i></span></span>
      </div>
    </li>
    <li class="pub-item">
      <span class="pub-num">[17]</span>
      <div class="pub-body">
        <strong class="title">Promoting Self-Efficacy of Individuals With Autism in Practicing Social Skills in the Workplace Using Virtual Reality and Physiological Sensors: Mixed Methods Study</strong><br>
        SI Kim, S Jang, T Kim, <strong><u>B Kim</u></strong>, D Jeong, T Noh, M Jeong, K Hall, M Kim, HJ Yoo, K Han, H Hong, and JG Kim<br>
        <span class="venue journal"><strong>JMIR Formative Research</strong><span class="venue-note"> (SCIE, 2024.01)</span></span>
      </div>
    </li>
    <li class="pub-item">
      <span class="pub-num">[16]</span>
      <div class="pub-body">
        <strong class="title">V-DAT: Supporting Self-Awareness for Autistic People from Multimodal VR Sensor Data</strong><br>
        <strong><u>B Kim</u></strong>, D Jeong, JG Kim, H Hong, and K Han<br>
        <span class="venue conf"><strong>ACM UIST 2023</strong><span class="venue-note"> | <i>ACM International Symposium on User Interface Software and Technology</i></span></span>
      </div>
    </li>
    <li class="pub-item">
      <span class="pub-num">[15]</span>
      <div class="pub-body">
        <strong class="title">Supporting Independence of Autistic Adults through Mobile and Virtual Reality Technologies</strong><br>
        <strong><u>B Kim</u></strong><br>
        <span class="venue conf"><strong>ACM UIST 2023</strong><span class="venue-note"> (Doctoral Symposium) | <i>ACM International Symposium on User Interface Software and Technology</i></span></span>
      </div> 
    </li>
    <li class="pub-item">
      <span class="pub-num">[14]</span>
      <div class="pub-body">
        <strong class="title">RoutineAid: Externalizing Key Design Elements to Support Daily Routines of Individuals with Autism</strong><br>
        <strong><u>B Kim</u></strong>, S-I Kim, S Park, HJ Yoo, H Hong, and K Han<br>
        <span class="venue conf"><strong>ACM CHI 2023</strong><span class="venue-note"> | <i>ACM International Conference on Human Factors in Computing Systems</i></span></span>
      </div>
    </li>
    <li class="pub-item">
      <span class="pub-num">[13]</span>
      <div class="pub-body">
        <strong class="title">VISTA: User-centered VR Training System for Effectively Deriving Characteristics of People with Autism Spectrum Disorder</strong><br>
        <strong><u>B Kim</u></strong>, D Jeong, M Jeong, T Noh, SI Kim, T Kim, S Jang, HJ Yoo, JG Kim, H Hong, and K Han<br>
        <span class="venue conf"><strong>ACM VRST 2022</strong><span class="venue-note"> | <i>ACM International Symposium on Virtual Reality Software and Technology</i></span></span>
      </div>
    </li>
	<li class="pub-item">
      <span class="pub-num">[12]</span>
      <div class="pub-body">
        <strong class="title">A Study on Mobile Game Design to Support Daily Routines of Individuals with Autism</strong><br>
        <strong><u>B Kim</u></strong>, S-I Kim, S Park, H Hong, and K Han<br>
        <span class="venue journal"><strong>Journal of HCI Korea</strong><span class="venue-note"> (2022.06)</span></span>
      </div>
    </li>
    <li class="pub-item">
      <span class="pub-num">[11]</span>
      <div class="pub-body">
        <strong class="title">A Systematic Review on Fake News Research through the Lens of News Creation and Consumption: Research Efforts, Challenges, and Future Directions</strong><br>
        <strong><u>B Kim</u></strong>, A Xiong, D Lee, and K Han<br>
        <span class="venue journal"><strong>PLoS One</strong> <span class="venue-note">(SCIE, 2021.12)</span></span>
      </div>
    </li>
    <li class="pub-item">
      <span class="pub-num">[10]</span>
      <div class="pub-body">
        <strong class="title">ChamberBreaker: Mitigating the Echo Chamber Effect and Supporting Information Hygiene through a Gamified Inoculation System </strong><br>
        Y Jeon, <strong><u>B Kim</u></strong>, A Xiong, D Lee, and K Han<br>
        <span class="venue conf"><strong>ACM CSCW 2021</strong> <span class="venue-note"> | <i>ACM International Conference on Computer-Supported Cooperative Work & Social Computing</i></span></span>
      </div>
    </li>
    <li class="pub-item">
      <span class="pub-num">[9]</span>
      <div class="pub-body">
        <strong class="title">Usability Assessment of a Mobile Health Intervention for Increasing Physical Activity in Autistic Adults </strong><br>
        D Lee, G Frey, A Min, <strong><u>B Kim</u></strong>, D Cothran, S Bellini, K Han, and PC Shih<br>
        <span class="venue journal"><strong>SAGE Health Informatics Journal,</strong> <span class="venue-note">(SCIE, 2020.09)</span></span>
      </div>
    </li>
    <li class="pub-item">
      <span class="pub-num">[8]</span>
      <div class="pub-body">
        <strong class="title">PuzzleWalk: A Theory-Driven Iterative Design Inquiry of a Mobile Game for Promoting Physical Activity in Autistic Adults</strong><br>
        <strong><u>B Kim</u></strong>, D Lee, A Min, S Paik, G Frey, S Bellini, K Han, and PC Shih<br>
        <span class="venue journal"><strong>PLoS One</strong> <span class="venue-note">(SCIE, 2020.09)</span></span>
      </div>
	   <li class="pub-item">
      <span class="pub-num">[7]</span>
      <div class="pub-body">
        <strong class="title">Ecological Momentary Assessment of Physical Activity, Sedentary Time, and Anxiety in Autistic Adults</strong><br>
        DH Lee, D Cothran, S Bellini, PC Shih, K Han, <strong><u>B Kim</u></strong>, A Min, S Paik, and GC Frey<br>
        <span class="venue conf"><strong>INSAR 2020</strong> <span class="venue-note">(Poster) | International Society for Autism Research</span></span>
      </div>
    </li>
	 <li class="pub-item">
      <span class="pub-num">[6]</span>
      <div class="pub-body">
        <strong class="title">Objectively Measured Physical Activity and Sedentary Time in Adults with Autism Spectrum Disorder</strong><br>
        DH Lee, PC Shih, <strong><u>B Kim</u></strong>, K Han, A Min, D Cothran, S Bellini, and GC Frey<br>
        <span class="venue journal"><strong>Medicine and Science in Sports and Exercise</strong> <span class="venue-note">(2020.07)</span></span>
      </div>
    </li>
    </li>
    <li class="pub-item">
      <span class="pub-num">[5]</span>
      <div class="pub-body">
        <strong class="title">No More One Liners: Bringing Context into Emoji Recommendations</strong><br>
        J-G Kim, T Gong, <strong><u>B Kim</u></strong>, JY Park, W Kim, E Huang, K Han, J Kim, JG Ko, and SJ Lee<br>
        <span class="venue journal"><strong>ACM Transactions on Social Computing</strong> <span class="venue-note">(2020.04)</span></span>
      </div>
    </li>
    <li class="pub-item">
      <span class="pub-num">[4]</span>
      <div class="pub-body">
        <strong class="title">ATM: The Effectiveness of Self-Regulation on Time Management through a Smartphone Application</strong><br>
       <strong><u>B Kim</u></strong>, S-W Lee, H Hong, and K Han<br>
        <span class="venue journal"><strong>IEEE Access</strong> <span class="venue-note">(SCIE, 2019.07)</span></span>
      </div>
    </li>
   <li class="pub-item">
      <span class="pub-num">[3]</span>
      <div class="pub-body">
        <strong class="title">Bringing Context into Emoji Recommendations</strong><br>
        J-G Kim, T Gong, <strong><u>B Kim</u></strong>, JY Park, W Kim, E Huang, K Han, J Kim, JG Ko, and S-J Lee<br>
        <span class="venue conf"><strong>ACM MobiSys 2019</strong> <span class="venue-note">(Poster) | <i>ACM International Conference on Mobile Systems, Applications, and Services</i></span></span>
      </div>
    </li>
	<li class="pub-item">
      <span class="pub-num">[2]</span>
      <div class="pub-body">
        <strong class="title">Leveraging Mobile Technology to Support Goal Setting and Strategies of College Students</strong><br>
        <strong><u>B Kim</u></strong>, S Rhim, K Han, and S-W Lee<br>
        <span class="venue conf"><strong>ACM UbiComp 2018</strong> <span class="venue-note">(Poster) | <i>ACM International Conference on Pervasive and Ubiquitous Computing</i></span></span>
      </div>
    </li>
    <li class="pub-item">
      <span class="pub-num">[1]</span>
      <div class="pub-body">
        <strong class="title">Photos Don't Have Me, But How Do You Know Me?: Analyzing and Predicting Users on Instagram</strong><br>
        K Han, Y Jo, Y Jeon, <strong><u>B Kim</u></strong>, J Song, and SW Kim<br>
        <span class="venue conf"><strong>UMAP 2018</strong> <span class="venue-note">(Short) | <i>ACM International Conference on on User Modeling, Adaptation and Personalization</i></span></span>
      </div>
    </li>
  </ul>
</div>
		

<div id="honors" class="section">
    <h5 class="section-title">Honors & Awards</h5>
    <hr class="sep">
    <ul class="my_list">
        <li> <strong class="title">Best Paper Honorable Mention</strong> <br>
            ACM CHI conference on Human Factors in Computing Systems <span class="dot-sep"></span> 2026
        </li>
        <li> <strong class="title">Jang Young Sil Fellowship</strong> <br>
            Ministry of Science and ICT, Korea<span class="dot-sep"></span> 2025
        </li>
        <li> <strong class="title">NRF of Korea Ph.D. Fellowship</strong> <br>
            National Research Foundation of Korea<span class="dot-sep"></span> 2023
        </li>
        <li> <strong class="title">UIST Travel Grant</strong> <br>
            ACM Symposium on User Interface Software and Technology <span class="dot-sep"></span> 2023
        </li>
        <li> <strong class="title">Gary Marsden Travel Award</strong> <br>
            SIGCHI <span class="dot-sep"></span> 2023
        </li>
        <li><strong class="title">SK Creative Challenge Finalist</strong> <br>
            SK C&C <span class="dot-sep"></span> 2022
        </li>
        <li><strong class="title">IITP Best Global Research Team Award</strong> <br>
            Institute of Information & communications Technology Planning & Evaluation <span class="dot-sep"></span> 2021
        </li>
        <li><strong class="title">IITP High-Potential Individuals Global Training Fellowship</strong> <br>
            Institute of Information & communications Technology Planning & Evaluation <span class="dot-sep"></span> 2020
        </li>
        <li><strong class="title">Global Talent Attraction Program (GTAP) Fellowship</strong> <br>
            Indiana University <span class="dot-sep"></span> 2019
        </li>
        <li><strong class="title">Honors on the Dean's List</strong> <br>
            Academic Honors <span class="dot-sep"></span> 2011, 2012, 2015
        </li>
        <li><strong class="title">Global Excellence Scholarship</strong> <br>
            Merit-based Scholarship <span class="dot-sep"></span> 2011
        </li>
        <li><strong class="title">Special Recognitions for Outstanding Reviews</strong> <br>
            CHI 2024, CHI 2025, IMWUT 2025, CHI 2026
        </li>
        <li><strong class="title">Domestic Conference Awards</strong> <br>
            Grand Paper Award: KDMS 2024 <br>
            Best Paper Award: KDMS 2024 <br>
            Best Presentation Award: KCC 2024
        </li>
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
