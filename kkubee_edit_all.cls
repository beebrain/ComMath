% *** kkuthesis.cls ***
% A Class to create a thesis that complies Khon Kaen University Thesis Guidelines.
% by 
% Kittiphong Meesawat - jarkmeesawat@gmail.com
% Aditap Khongjun - sc-physics@hotmail.com
% 09 Nov 2010

% English Thesis support and 
% Separate ambiguous commands that can be both Thai or English 
% into appropriate form, default in English and adding 'th' after the command
% for Thai commands eg. title (English) and titleth(Thai) 
% by Seksan Poltree - seksan.poltree@gmail.com


% Identification
\ProvidesPackage{kkubee_edit_all}[2010/11/09 Khon Kaen University Thesis Class]

% This class is based on the standard report class.
% It should have option to process twoside report too.
\LoadClass[fleqn,fontsize=16pt,a4paper,oneside]{book}

% This class is currently support only Thai thesis.
% To support English thesis, some works on options 
% must be taking care of.

\RequirePackage{xltxtra}
\RequirePackage{xunicode}


\usepackage{etoolbox}
\RequirePackage{fontspec}
\RequirePackage{xunicode}
\RequirePackage{amsthm}
\XeTeXlinebreaklocale 'th_TH'
\XeTeXlinebreaklocale "th"
\XeTeXlinebreakskip = 0pt plus 1pt
\hyphenpenalty=10000
\renewcommand{\baselinestretch}{1.2}

\linespread{1.2}
\defaultfontfeatures{Scale=1.35}
\usepackage{hyperref} 
\usepackage{emptypage}


\renewcommand{\Huge}{\fontsize{16pt}{22pt}\selectfont}		%% 20pt in word
\renewcommand{\small}{\fontsize{10pt}{14pt}\selectfont}
\renewcommand{\normalsize}{\fontsize{11pt}{15.5pt}\selectfont}	%%16pt in word
\renewcommand{\large}{\fontsize{12pt}{17pt}\selectfont}   %%% 18pt in word



%% math define 
%Add example
\usepackage[fleqn]{amsmath}  % fleqn = จัดสมการ display ชิดซ้าย (สม่ำเสมอทั้งเล่ม)
\usepackage{amsthm}
%\theoremstyle{plain}
\newtheoremstyle{mytheoremstyle} % name
    {\topsep}                    % Space above
    {\topsep}                    % Space below
    {}                   % Body font
    {}                           % Indent amount
    {\scshape}                   % Theorem head font
    {}                          % Punctuation after theorem head
    {.5em}                       % Space after theorem head
    {}  % Theorem head spec (can be left empty, meaning ‘normal’)

\theoremstyle{mytheoremstyle}
\newtheorem{thm}{ทฤษฎีบท}[chapter] % reset theorem numbering for each chapter
\newtheorem{defn}{บทนิยาม}[chapter]  % definition numbers are dependent on theorem numbers
\newtheorem{exmp}[thm]{ตัวอย่าง} % same for example numbers
\usepackage[utf8]{inputenc}
\usepackage{enumitem} %adding itemize
%\setlist[enumerate]{leftmargin=0cm,itemindent = 2.15 cm, itemsep = 0em,topsep=0em,labelsep = 0.3cm,wide = 0pt,labelwidth = 1.25em}
\renewcommand{\labelenumii}{\theenumii}
\renewcommand{\theenumii}{\theenumi.\arabic{enumii}.}
\renewcommand{\labelenumiii}{\theenumiii}
\renewcommand{\theenumiii}{\theenumii\arabic{enumiii}.}
\setlist[itemize]{leftmargin = 1.8em, labelindent = 0.6em, topsep = 0.1em, itemsep = 0.05em, parsep = 0pt}
\setlist[enumerate,1]{leftmargin = 2.2em,
labelindent = 0.8em,
labelwidth = 1.4em,
labelsep = 0.4em,
topsep = 0.1em,
itemsep = 0.05em,
parsep = 0pt}
\setlist[enumerate,2]{leftmargin = 3.6em,
labelindent = 1.6em,
labelwidth = 1.8em,
labelsep = 0.4em,
topsep = 0.1em,
itemsep = 0.05em,
parsep = 0pt}

\setlist[enumerate,3]{leftmargin = 5.0em,
	labelindent = 2.4em,
	labelwidth = 2.2em,
	labelsep = 0.4em,
	topsep = 0.1em,
	itemsep = 0.05em,
	parsep = 0pt}

% Optional package
\usepackage{multirow}

%add subfigures
\usepackage{graphicx}
\usepackage{subcaption}
%\renewcommand\thesubfigure{\arabic{subfigure}}
\usepackage{adjustbox} %adjusted table

%%%%%Add clear leftpage to new page
\newcommand*\cleartoleftpage{%
  \clearpage
  \ifodd\c@page\relax
  \else
    \hbox{}\vspace*{\fill}\thispagestyle{empty}\newpage
  \fi
}


%%%%%Add source if some tables and figures are needed to citation
\newcommand*{\captionsource}[2]{%
	\caption[{#1}]{#1%
		\\%
		\noindent ที่มา: #2%
	}%
}

%%%%%%%%%%%%%%%%%%%%%%  define ref style


\usepackage[
backend=biber,
bibencoding=utf8,
refsegment=chapter,
style=apa6,
citestyle=authoryear,
firstinits=true,
isbn=false,
doi=false,
url=false,
sorting=nyt,
clearlang=true,
natbib=true,
%intitle=true,
date=year,
uniquelist=false,
minbibnames=6,
maxbibnames=6,
maxcitenames=6,
maxnames = 6,
defernumbers=true,
eprint=false
]{biblatex}

%%%%%%%%%%% change and to & for citation and bib
\renewcommand*{\finalnamedelim}{%
  \ifnumgreater{\value{liststop}}{2}{\finalandcomma}{}%
  \addspace\&\space}
  
\DeclareFieldFormat[article,unpublished,misc,book]{title}{\textit{#1}}
\DeclareFieldFormat[article,unpublished,misc,book]{journaltitle}{\text{#1}}

%% change vertical space between title ref and item ref



%% importance section. This section is reformat author style.
%% If the author name over than 6 people. It will added et al. at the 6 th position.
%% If you want to change the maximum author name. Please change \maxprtauth to the number that you want.
\renewcommand{\maxprtauth}{6}

\AtEveryBibitem{\clearfield{labelmonth}}
\AtEveryBibitem{\clearfield{labelday}}
\AtEveryCitekey{\clearfield{labelmonth}}
\AtEveryCitekey{\clearfield{labelday}}
\AtEveryBibitem{
	\clearfield{labelmonth}
	\clearfield{doi}
	\ifentrytype{inproceedings}{
		\clearfield{volume}%%
		\clearfield{editor}
	}{}
}


\renewbibmacro*{title}{%
  \ifthenelse{\iffieldundef{title}\AND\iffieldundef{subtitle}}
    {\printfield{titleaddon}}
    {\iffieldundef{origtitle}
      {\printtext[title]{%
        \printfield[apacase]{title}%
        \setunit{\subtitlepunct}%
        \printfield[apacase]{subtitle}}}
      {\printfield{origtitle}%
       \setunit{\addspace}%
       \printtext[brackets]{%
        \printfield[apacase]{title}%
        \setunit{\subtitlepunct}%
        \printfield[apacase]{subtitle}}}%
     \setunit{\addspace}%
     \ifentrytype{inbook}{}{\setunit*{\addperiod\printtext{~~}} \printfield{edition}}% additional info in parens
     \setunit{\addspace}%
     \printfield{titleaddon}%
     \setunit{\addspace}%
     }}%


\DeclareBibliographyDriver{book}{%
  \usebibmacro{bibindex}%
  \usebibmacro{begentry}%
  \usebibmacro{author/editor}%
  \setunit{\printdelim{nametitledelim}}\newblock
  \setunit{\addperiod\printtext{~~}}
  \usebibmacro{maintitle+title}%
  \newunit\newblock
  \usebibmacro{location+publisher}
  \newunit\newblock
  \printfield{addendum}%
  \newunit\newblock
  \iftoggle{bbx:related}
    {\usebibmacro{related:init}%
     \usebibmacro{related}}
    {}%
  \usebibmacro{pageref}%
  \usebibmacro{annotation}%
  \usebibmacro{finentry}}



\patchcmd{\thebibliography}{\chapter*}{\section*}{}{}
\setlength\bibhang{1.5cm}

  
%%%%%%%%%%%%%%%%%%%
%\setotherlanguages{english}
%\setmainlanguage{thai} %% or other languages



%\setmainfont[%
%Extension = .ttf,
%Script=Thai,
%Scale=1.5,
%WordSpace=1,
%ItalicFont={TH Sarabun New Italic},
% BoldFont={TH Sarabun New Bold},
% BoldItalicFont={TH Sarabun New Bold Italic} ,
% NFSSFamily=sarabun
% ]
% {TH Sarabun New}
\setmainfont[Script=Thai,WordSpace=1,Scale=1.5]{TH Sarabun New}
%\newfontfamily\thaifont[Extension = .TTF,Script=Thai,Scale=1.5,ItalicFont={TH Sarabun New Italic}, BoldFont={TH Sarabun New Bold},BoldItalicFont={TH Sarabun New Bold Italic} ]{TH Sarabun New}
%\newfontfamily\thaifont[Script=Thai,Scale=1.5,ItalicFont={TH Sarabun New Italic}, BoldFont={TH Sarabun New Bold},BoldItalicFont={TH Sarabun New Bold Italic} ]{TH Sarabun New}


% line spacing entire document for English thesis is 1.5x
% \selectfont



% Layout packages
\RequirePackage[a4paper, twoside, top=30mm, bottom=25mm, inner=30mm, outer=20mm, headheight=14pt]{geometry}
\RequirePackage{fancyhdr}
\RequirePackage{calc}
\RequirePackage{indentfirst}                                                                                                          
\RequirePackage{titlesec}
\RequirePackage{titletoc}
\RequirePackage{ifthen}
\RequirePackage{lineno}

% More declarations
% Page margins
% If number of pages does not exceed 170pages, we can use one side print
% Use two pages
%\geometry{a4paper, twoside, top=1.5in, bottom=1in, left=1in, right=1in, headsep=0.8in}
%\geometry{a4paper, top=1.5in, bottom=1in, left=1in, right=1in, headsep=0.8in}
%\geometry{bindingoffset=0.5in} 


% Paragraph Indentation
% Indent 6 characters, paragraph begins at character 7
% The next level of section requires 6 more characters
% for the indentation
\def\firstindentlength{1cm}   %% five character aproximate 1 cm
\def\secondindentlength{2cm} 
\def\thirdindentlength{3cm}
\def\fourthindentlength{4cm}

\setlength{\parindent}{1.5cm}
\setlength{\itemsep}{1cm}

\RequirePackage[singlelinecheck=false]{caption} 
\RequirePackage{remreset} % I use this just to renew the figure and table counters.

% Graphic package (required here because the thesis must 
% have the university logo on the cover and on the title page)
\RequirePackage{graphicx}
\RequirePackage{intcalc}
\RequirePackage{fontspec}

% Float page alignment margin to top margin
\setlength{\@fptop}{0pt}


% Disable space between chapter in lot and lof
% from http://tex.stackexchange.com/questions/784/how-to-change-the-line-spacing-in-my-list-of-figures/793#793
%\renewcommand{\small}{\fontsize{11}{13}\selectfont}
%\renewcommand{\normalsize}{\fontsize{12}{14}\selectfont}
%\renewcommand{\large}{\fontsize{14}{16}\selectfont}

\newcommand*{\noaddvspace}{\renewcommand*{\addvspace}[1]{}}
\addtocontents{lof}{\protect\noaddvspace} % for figure
\addtocontents{lot}{\protect\noaddvspace} % for table

\setcounter{tocdepth}{1}

\renewcommand\tableofcontents{%
	\chapter*{\centering \large \textbf{สารบัญ}}%
	\begin{flushright}%
		\textbf{หน้า}%
	\end{flushright}%
	\vspace{-0.5em}%
	\@starttoc{toc}%
	\clearpage
}

\titlecontents{chapter}
[0pt]
{\addvspace{0.75em}\bfseries}
{\thecontentslabel\quad}
{}
{\titlerule*[0.5pc]{.}\contentspage}

\titlecontents{section}
[1.5em]
{\addvspace{0.25em}}
{\thecontentslabel\quad}
{}
{\titlerule*[0.5pc]{.}\contentspage}

\titlecontents{subsection}
[3.0em]
{\addvspace{0.15em}\small}
{\thecontentslabel\quad}
{}
{\titlerule*[0.5pc]{.}\contentspage}

% List of Tables
\renewcommand\listoftables{%
	\chapter*{\centering \large \textbf{สารบัญตาราง}}%
	\addcontentsline{toc}{chapter}{สารบัญตาราง}%
	\begin{flushright}%
		\textbf{หน้า}%
	\end{flushright}%
	\vspace{-0.5em}%
	\@starttoc{lot}%
	\clearpage
}

\renewcommand{\tablename}{}
\titlecontents{table}
[0pt]
{\addvspace{0.25em}}
{ตารางที่~\thecontentslabel\quad}
{}
{\titlerule*[0.5pc]{.}\contentspage}

% List of Figures
\renewcommand\listoffigures{%
	\chapter*{\centering \large \textbf{สารบัญภาพ}}%
	\addcontentsline{toc}{chapter}{สารบัญภาพ}%
	\begin{flushright}%
		\textbf{หน้า}%
	\end{flushright}%
	\vspace{-0.5em}%
	\@starttoc{lof}%
	\clearpage
}

\renewcommand{\figurename}{}
\titlecontents{figure}
[0pt]
{\addvspace{0.25em}}
{ภาพที่~\thecontentslabel\quad}
{}
{\titlerule*[0.5pc]{.}\contentspage}


%%%%%%%%%%%%%% redefine content name
\renewcommand{\bibname}{บรรณานุกรม}
\renewcommand{\contentsname}{\begin{center} 
				{\large \textbf{สารบัญ}}
			\end{center}
}
\renewcommand{\chaptername}{}




% Chapter Style
% Question! - The thesis manual requires that the space between the chapter heading 
% and the first paragraph is 2 lines. How long is 2 lines? Absolute (like I did) or 
% relative shall be used?
%\renewcommand{\@makechapterhead}[1]{%
%% Does center environment effect on the vertical space?
%% Is 45 points enough for 2 lines?
%\thispagestyle{empty}
%	\begin{center} 
%		{\large \textbf{ \MakeUppercase\@chapapp\space  ~\thechapter} \\ \textbf{#1}}
%	\end{center}
%	\vspace{\baselineskip}
%}


%\titleformat{\chapter}[display]
%{\normalfont\bfseries}{}{10pt}{\large \textbf{ บทที่\space  ~\thechapter} \\ \textbf{#1}}

\def\thechapter{\arabic{chapter}}
\titleformat{\chapter}[display]
  {\Huge\bfseries\filcenter}{}{0pt}{\Huge}
\titlespacing*{\chapter}
  {0pt}{0pt}{22pt}
\assignpagestyle{\chapter}{empty}
%%%%%%%%%%%%%%%%%%%%% addition new command %%%%%%%%%%%%%%%%
\newcommand\blfootnote[1]{%
	\begingroup
	\renewcommand\thefootnote{}\footnote{#1}%
	\addtocounter{footnote}{-1}%
	\endgroup
}


%section style setup
% Fix: Added proper label width (1.5em) to prevent section number overlap with title text
% Also increased beforeskip from 0ex to 1ex for better spacing before section titles
\providecommand\thesection{}
\titleformat{\section}{\large\bfseries\upshape}{\thesection}{0.5em}{}
\titlespacing{\section}{0ex}{1ex}{\parskip}
% set indent of section
\let\oldsection\section
\def\section{\setlength{\parindent}{1.5cm}\oldsection}

%%subsection setup 
% Fix: Added proper label width (2em) to prevent subsection number overlap with title text
\providecommand\thesubsection{}
\titleformat{\subsection}{\bfseries\upshape}{\thesubsection}{0.5em}{}
\titlespacing{\subsection}{1.5cm}{1ex}{\parskip}
% set indent of subsection
\let\oldsubsection\subsection
\def\subsection{\setlength{\parindent}{1.5cm}\oldsubsection}





%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%End section Style %%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%% caption style %%%%%%%%%%%%%%%%%%%%%%
\DeclareCaptionLabelSeparator{doublespace}{~}
% Redefine table caption style
\captionsetup[table]{format=plain,labelfont={up},textfont={md,up},labelsep=doublespace,
	justification=raggedright,name=ตารางที่}
\@removefromreset{table}{chapter}
\renewcommand\thetable{\arabic{table}}

% Redefine figure caption style
\captionsetup[figure]{format=plain,labelfont={up},textfont={md,up},labelsep=doublespace,
	justification=raggedright,name=ภาพที่}
\@removefromreset{figure}{chapter}

\renewcommand\thefigure{\arabic{figure}}

% Redefine equation label style
\renewcommand{\theequation}{\thechapter.\arabic{equation}}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Page numbering style %%%%%%%%%%%%%%%%%
% Page numbering style for the body of the thesis
% Redifined for twopage
\newcommand{\setkkupagestyle}{%
	\pagestyle{fancy}
	\fancyhf{}
	\renewcommand\headrulewidth{0.4pt}
	\fancyhead[LE,RO]{\thepage}
	\fancyhead[RE]{\small\itshape คณิตศาสตร์สำหรับคอมพิวเตอร์}
	\fancyhead[LO]{\small\itshape\leftmark}
	\pagenumbering{arabic}
}%


\newcommand{\setkkuinfofirst}{%
	\pagestyle{fancy}
	\renewcommand\headrulewidth{0pt}
	\lhead{} \chead{} \rhead{} 
	\lfoot{} \cfoot{} \rfoot{}
	\fancyhead[CE,CO]{\thepage} % option for twoside
	\pagenumbering{roman}
}%


%%% change the page number appearance
\let\savethepage\thepage
\newcommand{\parenpage}{\renewcommand{\thepage}{(\savethepage)}}
\newcommand{\noparenpage}{\renewcommand{\thepage}{\savethepage}}


%%%%%%%%%%%%%%% Generate Cover Pages section %%%%%%%%%%%%%%%%%%%%%%%%%
% - Thesis Information
% Thai commands
\newcommand*{\courseIdth}[1]{\def\@courseIdth{#1}}
\newcommand*{\titleth}[1]{\def\@titleth{#1}}
\newcommand*{\authora}[1]{\def\@authora{#1}} % author without title in English
\newcommand*{\authorth}[1]{\def\@authorth{#1}} % author with title in Thai
\newcommand*{\academicyearth}[1]{\def\@academicyearth{#1}}

\newcommand*{\degreeA}[1]{\def\@degreeA{#1}}
\newcommand*{\degreeB}[1]{\def\@degreeB{#1}}
\newcommand*{\degreeC}[1]{\def\@degreeC{#1}}

\newcommand*{\academicyearen}[1]{\def\@academicyearen{#1}}
%\newcommand*{\degree}[1]{\def\@degree{#1}}


% Abstract in Thai
\newcommand\abstractth{%
	\addcontentsline{toc}{chapter}{คำนำ}
		\thispagestyle{empty}
	\vspace{2.5mm}
	\begin{center}
		%\bfseries \abstractname
		\textbf{\large  คำนำ}
	\end{center}
	\vspace{2.5mm}
}

\renewcommand\maketitle{%
	
	%% clear page numbering
	\thispagestyle{empty}
	\pagestyle{empty}
	
	\begin{titlepage}
		\begin{center}
			{\Huge \textbf{{เอกสารคำสอน รหัสวิชา \@courseIdth}\\
					\vspace{0.5cm}	
					\textbf{\@titleth}}}
		\end{center}
		\vspace{7cm}
		\begin{center}
			{\Huge \textbf{\MakeUppercase{\@authorth}}}
		\end{center}
		\vspace{7cm}   %default \vspace{6.9cm}
		\begin{center}
			{\Huge \textbf{คณะวิทยาศาสตร์และเทคโนโลยี} \\
				\vspace{0.2cm}	
				\textbf{มหาวิทยาลัยราชภัฏอุตรดิตถ์} \\
				\vspace{0.2cm}
				\textbf{\@academicyearth}}
		\end{center}
		\newpage
		\cleardoublepage
	\end{titlepage}%

		\thispagestyle{empty}
	\mbox{}

}% End \maketitle

\newcounter{introChapter}
\newcommand\introChapter[1]{
	\thispagestyle{empty}
	\refstepcounter{introChapter}
	\chapter*{\centering \large  แผนการสอนประจำบทที่ \theintroChapter}
	\addcontentsline{toc}{chapter}{แผนการสอนประจำบทที่ \theintroChapter}
}

\newcommand\subtitle[1]{
	\hspace*{1.5cm}#1 \noindent 
}

\newcommand\subsubtitle[1]{
	\hspace*{2cm}#1 \noindent 
}


\newcommand\specialsection{%
  \titleformat*{\section}{\centering\scshape\large\bfseries\upshape}
}

\newcommand\regularsection{%
	\titleformat{\section}{\large\bfseries\upshape}{\thesection}{0.5em}{}
}

\newcommand\QAChapter{
  \clearpage
  \specialsection
	\section*{คำถามท้ายบทที่ \thechapter}
	\addcontentsline{toc}{section}{คำถามท้ายบทที่ \thechapter}
\regularsection
}

\newcommand\RefChapter{
\specialsection
	\section*{เอกสารอ้างอิง}
	\addcontentsline{toc}{section}{เอกสารอ้างอิง}
\regularsection

{\let\newpage\relax
\printbibliography[segment=\therefsegment,heading=none]}

}
\newcounter{sheetChapter}
\setcounter{sheetChapter}{1}
\newcommand\sheetChapter[1]{
  \specialsection
	\section*{ใบงานที่ \thesheetChapter}
	\addcontentsline{toc}{section}{ใบงานที่ \thesheetChapter}
	\section*{#1}
	\stepcounter{sheetChapter}
\regularsection
}

\usepackage{multido}
%%% newcommand for pointline
\newcommand{\Pointilles}[1]{%
  \par\nobreak
  \noindent\rule{0pt}{1.5\baselineskip}% Provides a larger gap between the preceding paragraph and the dots
  \multido{}{#1}{\noindent\makebox[\linewidth]{\dotfill}\endgraf}% ... dotted lines ...
  \bigskip% Gap between dots and next paragraph
}





