import streamlit as st
import random

# --------------------------------------------------
# CONFIGURATION DE LA PAGE
# --------------------------------------------------

st.set_page_config(
    page_title="Quiz d'histoire moderne",
    page_icon="💖",
    layout="centered"
)


# --------------------------------------------------
# QUESTIONS DU QUIZ
# Modifie les textes, mais conserve la structure.
#
# "correcte": 0 signifie réponse A
# "correcte": 1 signifie réponse B
# "correcte": 2 signifie réponse C
# "correcte": 3 signifie réponse D
# --------------------------------------------------

questions = [
    {
        "question": "Question : Quel enchaînement explique le mieux le départ de Christophe Colomb vers l'Ouest en 1492 ?",
        "propositions": [
            "A. La chute de Constantinople ferme totalement les routes vers l'Asie, tandis que le traité d'Alcaçovas réserve les Canaries au Portugal",
            "B. Le traité d'Alcaçovas limite l'expension Castillane vers les côtes africaines, ce qui encourage la monarchie espagnole à rechercher une autre route vers l'Asie par l'Ouest ",
            "C. Le portugal abandonne la route du contournement de l'Afrique après l'échec de Bartolomeus Dias au cap de Bonne-Espérance",
            "D. La découverte de l'Amérique sur le planisphère de Waldseemuller convainc les souverains espagnols de financer le voyage de Christophe C"
        ],
        "correcte": 1,
        "explication": "A : Les Canaries reviennent à la Castille, non au Portugal. "
                       "/ C : Dias atteint bien le cap de Bonne-Espérance en 1488, et les explorateurs Portugais poursuivront cette route. "
                       "/ D : Le planisphère de Waldseemuller date de 1507, donc après le voyage de CC."
                       "/ C'est la B : Le traité d’Alcaçovas de 1479 reconnaît notamment au Portugal une position privilégiée sur les routes africaines, tandis que la Castille conserve les Canaries. Cette rivalité pousse l’Espagne à soutenir le projet de Colomb. "
    },
    {
        "question": "Question : Quelle proposition compare correctement le renforcement monarchique de la France et de l’Angleterre à la fin du XVe siècle ?",
        "propositions": [
            "A. En France, la mort de Charles le Téméraire en 1477 entraîne le rattachement de la Provence. En Angleterre, Henri VII épouse Anne de Bretagne afin de réconcilier les maisons de Lancastre et d'York.",
            "B. En France, l’Édit d’Union de 1491 rattache définitivement la Bretagne au royaume ; en Angleterre, la bataille de Bosworth de 1453 met fin à la guerre de Cent Ans et permet l’arrivée des Tudor.",
            "C. En France comme en Angleterre, le renforcement monarchique repose principalement sur la conquête militaire immédiate des territoires féodaux et conduit dès la fin du XVe siècle à la formation de deux États-nations modernes.",
            "D. En France, la monarchie se renforce après la guerre de Cent Ans et le recul des grandes principautés féodales, en Angleterre, Henri VII stabilise le royaume après les guerres des Deux-Roses en réunissant symboliquement les maisons de Lancastre et d’York."
        ],
        "correcte": 3,
        "explication": "A : confond les modalités de rattachement de la Provence et de la Bretagne, ainsi que les mariages dynastiques. "
                       "/ B : confond le mariage de 1491 avec l'édit d'union de 1532, Bosworth mauvaise date. "
                       "/ C : nimp c'est une centralisation progressive c'est pas tout de suite deux états-nations modernes. "
                       "/ C'est la D : En France, la fin de la guerre de Cent Ans en 1453 et la mort de Charles le Téméraire en 1477 affaiblissent de puissants rivaux féodaux et renforcent progressivement l’autorité royale. En Angleterre, la victoire d’Henri Tudor à Bosworth en 1485, puis son mariage avec Élisabeth d’York, permettent une réconciliation symbolique entre Lancastre et York."
    },
    {
        "question": "Question : Quelle proposition est juste ?",
        "propositions": [
            "A. Bartolomeu Dias atteint le cap de Bonne-Espérance en 1488 ; Vasco de Gama rejoint l’océan Indien en 1498-1499 ; Magellan revient en Espagne en 1522 après avoir accompli le premier tour du monde.",
            "B. Bartolomeu Dias atteint le cap de Bonne-Espérance en 1488 ; Vasco de Gama ouvre une route maritime vers l’océan Indien en contournant l’Afrique ; l’expédition de Magellan en 1519 n'est pas achevée par lui même en 1522",
            "C. Bartolomeu Dias atteint le cap de Bonne-Espérance en 1488 ; Vasco de Gama accomplit le premier tour du monde entre 1498 et 1499 ; ce sera Elcano qui terminera l'expédition de Magellan en 1522.",
            "D. Bartolomeu Dias atteint le cap de Bonne-Espérance en 1498 ; Vasco de Gama rejoint l’océan Indien ; l’expédition de Magellan est achevée par Elcano après la mort de Magellan aux Philipines"
        ],
        "correcte": 1,
        "explication": "A : Magellan ne revient pas en Espagne, il crève aux Philipines, c'est Elcano qui termine en 1522."
                       "/ C : c'est pas vasco de Gama le tour du monde, et confond les itinéraires."
                       "/ D : date de Dias fausse c'est 1488  "
    },
    {
        "question": "Question : Quelle proposition est vraie concernant le premier séjour de Vasco da Gama à Calicut en 1498 ?",
        "propositions": [
            "A. Dès son arrivée, Vasco de Gama retient les premiers habitants montés à bord afin de contraindre le Samorin à le recevoir, cette stratégie lui permet d’obtenir rapidement une exemption des droits de douane.",
            "B. Le Samorin refuse de recevoir Vasco da Gama parce qu’il le considère comme un simple pirate et que ses cadeaux ainsi que sa marchandises sont merdiques, les Portugais repartent donc sans avoir été autorisés à vendre leurs marchandises ni à acheter des épices.",
            "C. Vasco da Gama est reçu comme l’envoyé du roi du Portugal, mais ses cadeaux de merde et la faible valeur de ses marchandises fragilise sa position. Il obtient certaines possibilités de commerce sans obtenir les privilèges espérés, puis recourt à la prise d’otages lorsque des Portugais et leurs biens sont retenus à terre.",
            "D. La présentation de la lettre de Manuel Ier convainc le Samorin d’accorder aux Portugais un monopole commercial à Calicut ; les tensions ultérieures viennent du refus de Vasco da Gama de laisser un représentant portugais sur place."
        ],
        "correcte": 2,
        "explication": " A : inverse la chronologie : la prise d’otages ne se produit pas dès l’arrivée et elle ne permet pas d’obtenir une exemption douanière."
                       "/ B : Vasco de Gama est bien reçu en audience et les Portugais peuvent vendre certain produits et acheter des épices, même si les résulats commerciaux restent décevants."
                       "/ D : Vasco de gama n'obtient ni monopole ni privilèges majeurs, les tensions portent sur les marchandises, les paiements exigés et la détention de Portugais."
                       "/ C'est la C. "
    },
    {
        "question": "Question : Quelle proposition est vraie concernant la colonisation portugaise du Brésil entre 1500 et 1549 ?",
        "propositions": [
            "A. Après une première phase principalement consacrée à l'exploitation d'une ressource, Jean III organise en 1534 quinze lots formant quatorze capitaineries confiées à des donataires. Les difficultés rencontrées conduisent ensuite à l’installation, en 1549, d’un gouvernement général à Salvador, qui centralise davantage la colonie sans supprimer immédiatement toutes les capitaineries.",
            "B. Dès 1500, les Portugais développent une colonisation territoriale intensive fondée sur les plantations de sucre, les capitaineries créées en 1534 servent ensuite uniquement à organiser l’importation des esclaves africains.",
            "C. En 1534, Jean III reprend directement l’administration de l’ensemble du Brésil en nommant Tomé de Sousa gouverneur général,  ce dernier fonde São Vicente, avant de déplacer la capitale à Salvador en 1549.",
            "D. Les capitaineries héréditaires sont toutes des échecs et sont juridiquement abolies dès l’arrivée de Tomé de Sousa en 1549, qui remplace les donataires par des missionnaires jésuites chargés d’administrer la colonie."
        ],
        "correcte": 0,
        "explication": "B : inverse la chronologie, d'abord exploitation du bois-brésil domine, la colonisation demeure limitée, l'économie sucrière se développe après."
                       "/ C : confond 1534, date des capitaineries, et 1549 arrivée de Tomé de Sousa. Sao Vicente avait été fondée dès 1532, et non par Tomé de Sousa."
                       "/ D : certaines capitaineries (Pernambuco et Sao Vicente, réussisent relativement bien. Le gouvernement général ne fait pas disparaitre immédiatement les capitaineries. Les jésuites ont une fonction missionnaire, pas celle de remplacer administrativement les donataires."
                       "/ c'est la A."
    },
    {
        "question": "Question : Quelle proposition est vrai ? ",
        "propositions": [
            "A. Pizaro conquiert Tenochtitlan avec l’aide de peuples autochtones.",
            "B. Moctezuma est capturé lors de la chute de Tenochtitlan en 1521.",
            "C. L’Espagne installe quelques comptoirs commerciaux au Mexique.",
            "D. Les Tlaxcaltèques s’allient à Cortés contre les Aztèques"
        ],
        "correcte": 3,
        "explication": " A : Ce n'est pas Pizaro c'est Cortès."
                       "/ B : en 1521 c'est Cuauhtémoc qui est capturé par Moctezuma."
                       "/ C : nimp l'Espagne ne se contente pas d'installer des comptoirs commerciaux, ils prennent le contrôle du territoire de l'Empire aztèques et fondent la Nouvelle-Espagne, avec une administration, des impôts, contrôlent de la populations et exploitent les terres et les mines."
                       "/ C'est la D."
    },
    {
        "question": "Question : Quelle proposition est vraie ?",
        "propositions": [
            "A. L’espagnol nommé l'encomendero devient juridiquement propriétaire des populations indigènes qui lui sont attribuées. L'encomendero perçoit un tribu en échange de protection et d'évangélisation",
            "B. Les Nouvelles Lois instauré par la couronne, suite aux contestations de Bartolomé de las casas, abolissent l’encomienda et tous les systèmes de travail forcé dans l’Amérique espagnole.",
            "C. La mita est un système de travail libre et salarié instauré dans les mines de Potosi",
            "D. L’encomienda donne à un colon le droit de percevoir un tribut ou du travail, sans lui conférer juridiquement la propriété des indigènes."
        ],
        "correcte": 3,
        "explication": "A : confond encomienda avec l'esclavage juridique, en fait les indigènes ne sont pas légalement la propriété de l'encomendero, même si la contrainte peut produire un esclavage de fait."
                       "/ B : exagère les effets des Nouvelles Lois, elles limitent l'encomienda, mais rencontre une très forte résistance et ne font pas disparaître le travail contraint."
                       "/ C : la mita impose un travail forcé par roulement, notamment dans les mines."
                       "/ C'est la D."
    },
    {
        "question": "Question : Quelle proposition est vrai ?",
        "propositions": [
            "A. Les compagnies commerciales remplacent les monarchies dans l’expansion coloniale : elles agissent librement, sans soutien public, tandis que les États renoncent aux profits et au contrôle des territoires d’outre-mer.",
            "B. Le passage au modèle des compagnies correspond moins à un retrait de l’État qu’à une délégation de certaines fonctions : des capitaux privés financent les flottes et les comptoirs, tandis que la monarchie accorde des monopoles et des pouvoirs politiques ou militaires, prélève des taxes et bénéficie de l’expansion à moindre coût.",
            "C. L’Espagne et le Portugal créent les premières compagnies privées afin de conserver leur monopole en Asie, tandis que les Provinces-Unies et l’Angleterre maintiennent une colonisation entièrement financée et administrée par leurs souverains.",
            "D. L’union dynastique de l’Espagne et du Portugal entre 1580 et 1640 fusionne leurs empires et renforce durablement leur monopole, obligeant les compagnies hollandaises et anglaises à privilégier uniquement la conquête territoriale des Amériques."
        ],
        "correcte": 1,
        "explication": "C'est la B : La rupture ne consiste donc pas à passer d'un empire contrôlé par l'Etat à une expension totalement privée. Elle correspond au passage d'un Etat qui administre et finance directement l'expansion à un Etat qui délègue une partie de ses fonctions à des compagnies privées qu'il autorise, protège et fiscalise."
                       "/ A : fait disparaitre l'état alors qu'il accorde les chartes, les monopoles et les pouvoirs aux compagnies."
                       "/ C : inverse les modèles, les grandes compagnies apparaissent surtout chez les Hollandais, les Anglais, puis les Français."
                       "/ D : l'union dynastique n'était pas un succès durable, car elle expose les possessions portugaises aux ennemis de l'Espagne et contribue à leur fragilisation."
    },
    {
        "question": "Question : Où et quand les forces britanniques capitulent-elles face aux insurgés américains et à leurs alliés français ?",
        "propositions": [
            "A. Bataille de Saratoga 1777",
            "B. Bataille de Yorktown 1783",
            "C. Bataille de Saratoga 1780",
            "D. Bataille de Yorktown 1781 "
        ],
        "correcte": 3,
        "explication": "La capitulation britannique a lieu à Yorktown en 1781. Le traité de Paris de 1783 reconnaît ensuite officiellement l'indépendance des États-Unis."
    },
    {
        "question": "Question : Quel enchaînement résume correctement les conséquences des trois grandes guerres du XVIIIᵉ siècle ?",
        "propositions": [
            "A. La guerre de sucession d'Espagne se termine par le traité d'Utrech (1713-1714) et donne à la France le trône espagnol et le contrôle de l’Asiento ; la guerre de sucession d'Autriche profite à la prusse de Frédéric II  ; pendant la guerre de Sept Ans l'amérique française s'effondre. ",
            "B. La guerre de Succession d’Espagne entraîne l’union politique de la France et de l’Espagne ; la guerre de Succession d’Autriche donne la Silésie à la France ; la guerre de Sept Ans met fin à la présence britannique en Inde.",
            "C. La guerre de Succession d’Espagne installe un Bourbon sur le trône espagnol, mais renforce l’Angleterre dans l’Atlantique ; la guerre de Succession d’Autriche confirme la montée de la Prusse et ne permet pas à la France de consolider ses gains en Inde ; la guerre de Sept Ans consacre la domination coloniale britannique.",
            "D. Les trois guerres permettent à la France de renforcer progressivement son empire colonial, tandis que l’Angleterre se concentre exclusivement sur les conflits européens."
        ],
        "correcte": 2,
        "explication": "A : Tout est juste sauf que c'est pas la France qui a l'Asiento mais l'Angleterre."
                       "/ B : La silésie revient pas à la France mais à la Prusse."
                       "/ D : pas du tout, l'Angleterre renforce sa puissance maritime et commerciale."
                       "/ C'est la C : En fait, la France obtient parfois un avantage dynastique ou militaire mais cela reste assez ponctuelle, tandis que l'Angleterre se renforce et en 1763 elle devient la première puissance coloniale mondiale."
    },
    {
        "question": "Question : Quel port a armé le plus grand nombre d’expéditions négrières françaises ?",
        "propositions": [
            "A. Nantes",
            "B. La Rochelle",
            "C. Le Havre",
            "D. Le port qu'Épique"
        ],
        "correcte": 0,
        "explication": "Nantes 1 744 expéditions soit 43 à 44% des expéditions négrières françaises. Contre Le Havre 451, La Rochelle 448."
    },
    {
        "question": "Question : Quel texte législatif donne, sous Louis XIV, un cadre juridique à l’esclavage dans les colonies françaises d’Amérique ?",
        "propositions": [
            "A. La déclaration des droits de l'homme et du citoyen",
            "B. Le code couleur",
            "C. Le code-barres",
            "D. Le code noir"
        ],
        "correcte": 3,
        "explication": " Le code noir promulgué en mars 1685 sous Louis XIV, rédigé par Colbert, pas besoin d'expliquer pourquoi les autres sont fausses."
    },
    {
        "question": "Question : Quel État d’Afrique est généralement considéré comme le premier du monde musulman à avoir officiellement aboli l’esclavage par décision de son souverain ?.",
        "propositions": [
            "A. Le liberia",
            "B. L'éthiopie",
            "C. Le Maroc",
            "D. La Tunisie"
        ],
        "correcte": 3,
        "explication": "On remercie Ahmed Pacha Bey pour l'abolition en 1846. A savoir, c'est en Mauritanie le dernier Etat au monde a avoir officiellement aboli l'esclavage en 1981. "
    },
    {
        "question": "Question : Quel enchaînement décrit le mieux l’évolution de la présence française en Amérique du Nord entre 1524 et 1608 ?",
        "propositions": [
            "A. Verrazzano est envoyé par François Ier pour exploré la côte de l'Amérique du Nord, il fonde québec en 1524, Cartier développent le commerce des fourrures et Champlain poursuit l'expédition de Cartier sous Henri IV, et renforce les alliances avec les Hurons ",
            "B. Verrazzano et Cartier explorent les côtes et le Saint-Laurent en cherchant notamment une route vers l’Asie, puis Champlain fonde Québec en 1608 et appuie l’installation française sur le commerce des fourrures et des alliances autochtones",
            "C. Verrazzano démarre son expédition du port du Havre en 1517, Cartier fonde une colonie permanente à Hochelaga en 1535, qu’il renomme Montréal, puis Champlain déplace cette colonie à Québec en 1608.",
            "D. Verrazzano et Cartier recherchent tous deux une route vers l’Asie, Champlain fonde Québec en 1608, mais rompt avec cette logique d’exploration en privilégiant une conquête territoriale directe sans dépendre des réseaux commerciaux autochtones."
        ],
        "correcte": 1,
        "explication": "C'est la B : Verrazzano explore la côte Atlantique en 1524 pour le compte de François Ier, dans l'espoir de trouver uen route occidentale vers l'Asie. Cartier poursuit cette recherche par le Saint-Laurent dans les années 1530. Champlain marque ensuite une nouvelle étape avec la fondation de Québec en 1608, établissement permanent lié au commerce des fourrures et aux alliances avec les Innus, les Algonquins et les Hurons-Wendats."
    },
    {
        "question": "Question : Au début du XVIIᵉ siècle, des protestants séparatistes anglais refusent de se soumettre à l’Église d’Angleterre. Après s’être réfugiés dans les Provinces-Unies, une partie d’entre eux embarque sur le Mayflower en 1620. Quel enchaînement décrit correctement la fondation de Plymouth ?",
        "propositions": [
            "A. Les colons arrivés au Cap Cod, fondent la première implantation anglaise permanente d’Amérique, avec une charte le Mayflower Compact, leur permettant de s’établir à Plymouth et d'établir des alliances avec les peuples autochtones notamment les wampanoag.",
            "B. Arrivés au cap Cod en dehors du territoire prévu par leur autorisation, les colons signent le Mayflower Compact, s’installent à Plymouth et survivent notamment grâce à l’aide et à l’alliance de membres des peuples autochtones.",
            "C. Les séparatistes quittent directement l’Angleterre pour fonder Plymouth sur un territoire inhabité, puis choisissent William Bradford comme gouverneur envoyé par la monarchie anglaise.",
            "D. Les colons s’installent initialement à Jamestown, mais abandonnent cette colonie après un conflit religieux et fondent Plymouth sous la protection des autorités néerlandaises."
        ],
        "correcte": 1,
        "explication": "A : ce n'est pas Plymouth la 1ère implantation anglaise, c'est Jamestown qui est fondée en 1607 précède donc Plymouth de 13 ans."
                       "/ C : les séparatistes avaient d'abord vécu à Leyde et le territoire n'était pas originellement inhabité."
                       "/ D : Plymouth et Jamestown sont deux colonies distinctes, les colons de Plymouth restent des sujets du roi d'Angleterre."
                       "/ C'est la B : Les passagers du Mayflower devaient s'installer dans une zone relevant de la Virginie, mais ils atteignent le cap Cod ces connards. Comme ils se trouvent hors du territoire couvert par leur autorisation, ils concluent le Mayflower compact afin de former un corps politique, capable d'adopter ses propres règles. La colonie est ensuite établie à Plymouth, sur un territoire Wampanoag auparavant habité et fortement touché par une épidémie. En 1621, les colons concluent une alliance avec Ousamequin et bénéficient de connaissance transmises notamment par Tisquantum."
    }
]


# --------------------------------------------------
# APPARENCE DU JEU
# --------------------------------------------------

st.markdown(
    """
    <style>

    /* Fond rose lumineux */
    .stApp {
        background:
            radial-gradient(
                circle at 15% 20%,
                rgba(255, 255, 255, 0.95) 0px,
                rgba(255, 255, 255, 0.25) 3px,
                transparent 7px
            ),
            radial-gradient(
                circle at 80% 30%,
                rgba(255, 255, 255, 0.90) 0px,
                rgba(255, 255, 255, 0.20) 4px,
                transparent 8px
            ),
            radial-gradient(
                circle at 25% 75%,
                rgba(255, 255, 255, 0.85) 0px,
                rgba(255, 255, 255, 0.20) 3px,
                transparent 7px
            ),
            linear-gradient(
                135deg,
                #ffd6e7,
                #ffb8d7,
                #f9c5eb,
                #ffc1dc
            );

        background-size:
            180px 180px,
            250px 250px,
            220px 220px,
            100% 100%;

        font-family: Georgia, "Times New Roman", serif;
    }

    /* Titre principal */
    .titre-principal {
        text-align: center;
        color: #9c174f;
        font-size: 44px;
        font-weight: bold;
        line-height: 1.2;
        margin-top: 25px;
        margin-bottom: 25px;

        text-shadow:
            2px 2px 0 white,
            0 0 12px rgba(255, 255, 255, 0.9),
            0 0 20px rgba(210, 32, 112, 0.35);
    }

    /* Encadré des consignes */
    .consigne {
        max-width: 760px;
        margin: auto;
        padding: 24px 32px;
        text-align: justify;
        text-align-last: center;
        font-size: 21px;
        line-height: 1.7;
        color: #72123f;

        background: rgba(255, 255, 255, 0.65);
        border: 2px solid rgba(190, 33, 101, 0.35);
        border-radius: 25px;

        box-shadow:
            0 8px 25px rgba(150, 17, 73, 0.18),
            inset 0 0 20px rgba(255, 255, 255, 0.8);
    }

    .consigne-titre {
        display: block;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #b0185b;
        margin-bottom: 12px;
    }

    /* Carte contenant la question */
    .question-card {
        margin-top: 25px;
        margin-bottom: 20px;
        padding: 24px 30px;

        background: rgba(255, 255, 255, 0.72);
        border: 2px solid rgba(190, 33, 101, 0.35);
        border-radius: 25px;

        box-shadow:
            0 8px 25px rgba(150, 17, 73, 0.18),
            inset 0 0 20px rgba(255, 255, 255, 0.8);

        color: #72123f;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        line-height: 1.5;
    }

    /* Compteur de questions */
    .compteur {
        text-align: center;
        font-size: 19px;
        color: #9c174f;
        font-weight: bold;
        margin-top: 18px;
    }

    /* Style des propositions */
    div[role="radiogroup"] {
        background: rgba(255, 255, 255, 0.55);
        border-radius: 20px;
        padding: 16px 20px;
        border: 1px solid rgba(190, 33, 101, 0.25);
    }

    div[role="radiogroup"] label {
        font-size: 18px;
        color: #651239;
        padding: 7px;
    }

    /* Boutons */
    .stButton > button {
        width: 100%;
        border-radius: 22px;
        border: 2px solid #c51668;
        background: linear-gradient(135deg, #ff8fbd, #d9367d);
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 10px 18px;

        box-shadow:
            0 5px 15px rgba(170, 20, 88, 0.25),
            0 0 12px rgba(255, 255, 255, 0.6);
    }

    .stButton > button:hover {
        border-color: #921047;
        background: linear-gradient(135deg, #ffabd0, #c51668);
        color: white;
    }

    /* Score final */
    .score-final {
        margin-top: 25px;
        padding: 30px;
        text-align: center;
        font-size: 30px;
        font-weight: bold;
        color: #9c174f;

        background: rgba(255, 255, 255, 0.72);
        border: 2px solid rgba(190, 33, 101, 0.35);
        border-radius: 25px;

        box-shadow:
            0 8px 25px rgba(150, 17, 73, 0.18),
            inset 0 0 20px rgba(255, 255, 255, 0.8);
    }

    .etoiles {
        text-align: center;
        font-size: 28px;
        margin-top: 20px;
        color: #c51668;
        text-shadow: 0 0 10px white;
    }


    /* Carte rose affichée après une mauvaise réponse */
    .explication-card {
        margin-top: 18px;
        margin-bottom: 18px;
        padding: 20px 24px;

        background: rgba(255, 255, 255, 0.72);
        border: 2px solid rgba(190, 33, 101, 0.35);
        border-radius: 22px;

        box-shadow:
            0 8px 25px rgba(150, 17, 73, 0.18),
            inset 0 0 20px rgba(255, 255, 255, 0.8);

        color: #72123f;
        font-size: 18px;
        line-height: 1.6;
        text-align: justify;
    }


    /* --------------------------------------------------
       ADAPTATION POUR TÉLÉPHONE
    -------------------------------------------------- */

    @media screen and (max-width: 600px) {

        /* Réduit les marges générales de la page */
        .block-container {
            padding-left: 14px;
            padding-right: 14px;
            padding-top: 16px;
            padding-bottom: 24px;
        }

        /* Titre principal plus compact */
        .titre-principal {
            font-size: 29px;
            line-height: 1.25;
            margin-top: 8px;
            margin-bottom: 18px;
            padding-left: 4px;
            padding-right: 4px;
        }

        /* Consigne adaptée à la largeur du téléphone */
        .consigne {
            width: 100%;
            max-width: 100%;
            padding: 18px 15px;
            font-size: 17px;
            line-height: 1.5;
            border-radius: 18px;
            box-sizing: border-box;
            text-align: left;
            text-align-last: left;
            overflow-wrap: anywhere;
        }

        .consigne-titre {
            font-size: 23px;
            text-align: center;
            margin-bottom: 12px;
        }

        /* Carte de question */
        .question-card {
            width: 100%;
            max-width: 100%;
            padding: 18px 14px;
            font-size: 18px;
            line-height: 1.4;
            border-radius: 18px;
            box-sizing: border-box;
            overflow-wrap: anywhere;
            word-break: normal;
        }

        /* Compteur */
        .compteur {
            font-size: 16px;
            margin-top: 8px;
        }

        /* Propositions */
        div[role="radiogroup"] {
            width: 100%;
            box-sizing: border-box;
            padding: 11px 9px;
            border-radius: 16px;
        }

        div[role="radiogroup"] label {
            font-size: 15px;
            line-height: 1.35;
            padding: 7px 2px;
            align-items: flex-start;
        }

        div[role="radiogroup"] p {
            white-space: normal;
            overflow-wrap: anywhere;
            word-break: normal;
        }

        /* Boutons suffisamment grands pour le tactile */
        .stButton > button {
            font-size: 16px;
            padding: 10px 12px;
            border-radius: 18px;
            min-height: 48px;
        }

        /* Carte d’explication */
        .explication-card {
            width: 100%;
            max-width: 100%;
            padding: 17px 14px;
            font-size: 16px;
            line-height: 1.5;
            border-radius: 18px;
            box-sizing: border-box;
            text-align: left;
            overflow-wrap: anywhere;
            word-break: normal;
        }

        /* Score final */
        .score-final {
            width: 100%;
            max-width: 100%;
            padding: 22px 14px;
            font-size: 24px;
            border-radius: 18px;
            box-sizing: border-box;
        }

        .etoiles {
            font-size: 22px;
            margin-top: 14px;
        }

        /* Messages Streamlit */
        div[data-testid="stAlert"] {
            font-size: 15px;
            line-height: 1.4;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# MÉMOIRE DU JEU
# --------------------------------------------------

if "jeu_commence" not in st.session_state:
    st.session_state.jeu_commence = False

if "numero_question" not in st.session_state:
    st.session_state.numero_question = 0

if "score" not in st.session_state:
    st.session_state.score = 0.0

if "reponse_validee" not in st.session_state:
    st.session_state.reponse_validee = False

if "bonne_reponse" not in st.session_state:
    st.session_state.bonne_reponse = False

if "ordre_questions" not in st.session_state:
    st.session_state.ordre_questions = list(range(len(questions)))
    random.shuffle(st.session_state.ordre_questions)


# --------------------------------------------------
# FONCTION POUR RECOMMENCER
# --------------------------------------------------

def recommencer_quiz():
    st.session_state.jeu_commence = False
    st.session_state.numero_question = 0
    st.session_state.score = 0.0
    st.session_state.reponse_validee = False
    st.session_state.bonne_reponse = False
    st.session_state.ordre_questions = list(range(len(questions)))
    random.shuffle(st.session_state.ordre_questions)


# --------------------------------------------------
# TITRE
# --------------------------------------------------

st.markdown(
    """
    <div class="titre-principal">
        ✨ Quiz d'histoire moderne ✨<br>
        Niveau L1
    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# PAGE D'ACCUEIL
# --------------------------------------------------

if not st.session_state.jeu_commence:

    st.markdown(
        """
    <div class="consigne">
    <span class="consigne-titre">💖 Consigne 💖</span>
    Tu as une question et quatre propositions. Choisis la réponse qui te paraît correcte. Si le résultat apparaît en vert, c'est que tu as juste. S'il apparaît en rouge, c'est que tu es un 💖 idiot 💖.
    <br><br>
    <b>Une bonne réponse rapporte 1 point.</b>
    <br>
    <b>Une mauvaise réponse retire 0,2 point.</b>
    </div>
    <div class="etoiles">✦ ♡ ✧ ♡ ✦</div>
    """,
        unsafe_allow_html=True
    )

    if st.button("💖 Commencer le quiz 💖"):
        st.session_state.jeu_commence = True
        st.rerun()


# --------------------------------------------------
# ÉCRAN FINAL
# --------------------------------------------------

elif st.session_state.numero_question >= len(questions):

    # Empêche d'afficher une note négative
    note_finale = max(0, round(st.session_state.score, 1))

    st.markdown(
        f"""
        <div class="score-final">
            ✨ Quiz terminé ✨
            <br><br>
            Ta note est de :
            <br>
            {note_finale} / 15
        </div>
        """,
        unsafe_allow_html=True
    )

    if note_finale >= 13:
        st.success("C'est bien, tu gagnes un nude ou tu va te faire foutre, tu peux refaire le quiz sinon 💖")

    elif note_finale >= 10:
        st.success("C'est pas mal. Tu es un petit peu idiot ✨")

    elif note_finale >= 7.5:
        st.warning("Résultat moyen va réviser sale chien 💖")

    else:
        st.error("Retourne ouvrir ton cours immédiatement, trou de balle 💖")

    if st.button("🔄 Recommencer le quiz"):
        recommencer_quiz()
        st.rerun()


# --------------------------------------------------
# QUESTIONS
# --------------------------------------------------

else:

    numero = st.session_state.numero_question
    index_question = st.session_state.ordre_questions[numero]
    question_actuelle = questions[index_question]

    st.markdown(
        f"""
        <div class="compteur">
            Question {numero + 1} sur {len(questions)}
        </div>

        <div class="question-card">
            {question_actuelle["question"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    choix = st.radio(
        "Choisis une réponse :",
        question_actuelle["propositions"],
        index=None,
        key=f"reponse_{numero}",
        disabled=st.session_state.reponse_validee
    )

    # Bouton pour valider la réponse
    if not st.session_state.reponse_validee:

        if st.button("Valider ma réponse"):

            if choix is None:
                st.warning("Choisis d'abord une réponse.")

            else:
                index_choisi = question_actuelle["propositions"].index(choix)

                if index_choisi == question_actuelle["correcte"]:
                    st.session_state.score += 1
                    st.session_state.bonne_reponse = True

                else:
                    st.session_state.score -= 0.2
                    st.session_state.bonne_reponse = False

                st.session_state.reponse_validee = True
                st.rerun()

    # Affichage du résultat
    else:

        bonne_reponse = question_actuelle["propositions"][
            question_actuelle["correcte"]
        ]

        if st.session_state.bonne_reponse:
            st.success("Bonne réponse ! Tu n'es pas complètement perdue. 💖")

        else:
            st.error(
                f"T nul, tu as fait tes premiers pas dans l'escalier ?. La bonne réponse était : {bonne_reponse}"
            )

            st.markdown(
                f"""
                <div class="explication-card">
                    <b>💡 Explication :</b><br><br>
                    {question_actuelle["explication"]}
                </div>
                """,
                unsafe_allow_html=True
            )

        if st.button("Question suivante ➜"):
            st.session_state.numero_question += 1
            st.session_state.reponse_validee = False
            st.session_state.bonne_reponse = False
            st.rerun()