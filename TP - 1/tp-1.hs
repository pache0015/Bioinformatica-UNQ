data Base = A | T  | U  |  C  |  G  deriving Show
-- Invariante: Las cadenas de DNA se constituyen con bases del tipo: A C G T
-- Invariante: Las cadenas de RNA se constituyen con bases del tipo: A C G U

data Aminoacido = STOP | Phe  | Ser | Tyr | Cys | Leu  | Pro  | His  | Arg  |
               Trp  | Gln  | Ile | Thr  | Asn | Lys  | Gly  | Val | Ala | Asp |
               Glu  | Met  deriving Show
-- Invariante de representación: Las cadenas de Aminoacidos terminan en STOP.

type Proteina = [Aminoacido]
type X = Float
type Y = Float
type Z = Float
data Coordenada = Coor X Y Z deriving Show
data EstTerciaria = EstTer [ ( [Coordenada], EstSecundaria) ] deriving  Show
data EstSecundaria = BetaPlegada | AlphaHelice | Loop | SinForma deriving Show

type ADN = [Base]
type ARN = [Base]

transcribir :: ADN -> ARN
transcribir [] = []
transcribir (b : bs) = adn2arn b : transcribir bs

adn2arn :: Base -> Base
adn2arn T = U
adn2arn e = e

main :: ADN -> [Aminoacido]
main adn = segmentador (transcribir adn)

segmentador :: [Base] -> [Aminoacido]
segmentador (x: y : z : bs) = if isStop (formacionDeAminoacido x y z)
                    then segmentador []
                    else formacionDeAminoacido x y z : segmentador bs
segmentador _ = [STOP]

isStop :: Aminoacido -> Bool
isStop STOP = True
isStop _     = False

formacionDeAminoacido :: Base -> Base -> Base -> Aminoacido
-- Primer base U --
formacionDeAminoacido   U U U = Phe
formacionDeAminoacido   U U C = Phe
formacionDeAminoacido   U U _ = Leu
formacionDeAminoacido   U C _ = Ser
formacionDeAminoacido   U A U = Tyr
formacionDeAminoacido   U A C = Tyr
formacionDeAminoacido   U A _ = STOP
formacionDeAminoacido   U G A = STOP
formacionDeAminoacido   U G G = Trp
formacionDeAminoacido   U G _ = Cys
--Primer base C --
formacionDeAminoacido   C U _ = Leu
formacionDeAminoacido   C C _ = Pro
formacionDeAminoacido   C G _ = Arg
formacionDeAminoacido   C A U = His
formacionDeAminoacido   C A C = His
formacionDeAminoacido   C A _ = Glu
-- Primer base A --
formacionDeAminoacido   A U G = Met
formacionDeAminoacido   A U _ = Ile
formacionDeAminoacido   A C _ = Thr
formacionDeAminoacido   A A U = Asn
formacionDeAminoacido   A A C = Asn
formacionDeAminoacido   A A _ = Lys
formacionDeAminoacido   A G U = Ser
formacionDeAminoacido   A G C = Ser
formacionDeAminoacido   A G _ = Arg
-- Primer base G --
formacionDeAminoacido   G U _ = Val
formacionDeAminoacido   G C _ = Ala
formacionDeAminoacido   G A U = Asp
formacionDeAminoacido   G A C = Asp
formacionDeAminoacido   G A _ = Glu
formacionDeAminoacido   G G _ = Gly

-- Ejemplos de cadena adn --
cadena1 = [A,C,T,G,A,A,C,T,T,G,A,T,U,G,A]
cadena2 = [A,C,T,G,A,A,C,T,T,G,A,T,A]

prediccionEstSec :: Aminoacido -> EstSecundaria

prediccionEstSec STOP = SinForma

prediccionEstSec Ser = Loop
prediccionEstSec Pro = Loop
prediccionEstSec Asn = Loop
prediccionEstSec Gly = Loop
prediccionEstSec Asp = Loop

prediccionEstSec Tyr = BetaPlegada
prediccionEstSec Cys = BetaPlegada
prediccionEstSec Ile = BetaPlegada
prediccionEstSec Trp = BetaPlegada
prediccionEstSec Thr = BetaPlegada
prediccionEstSec Val = BetaPlegada
prediccionEstSec Phe = BetaPlegada

prediccionEstSec _ = AlphaHelice

