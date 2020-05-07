data Base = A | T  | U  |  C  |  G  deriving Show
-- Invariante: Las cadenas de DNA se constituyen con bases del tipo: A C G T
-- Invariante: Las cadenas de RNA se constituyen con bases del tipo: A C G U


type CadenaARN = [Base]
type Peptido = String

-- ## Casos ## --
sec1 = "TVAEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA"
secConTATA = "TATAAABBBBBTATAAA"
secConTATAbis = "TATAAABBBBBTATAAABABABA"
secSinTATA = "AAATATA"
secSinTATAFinal = "TATAAAAAAAA"
secSinTATAbis = "AAAAAAA"
secDeSoloTATA = "TATAAATATAAA"
secDeMuchosTATAS = "TATAAABTATAAABTATAAABTATAAA"


-- ## Reto 2 ## --
transform :: Peptido -> CadenaARN
transform [] = []
transform (x:xs) = deAminoABase x ++ transform xs

deAminoABase :: Char -> [Base]
deAminoABase 'A' = [ G , C , U ]
deAminoABase 'C' = [ U , G , U ]
deAminoABase 'D' = [ G , A , U ]
deAminoABase 'E' = [ G , A , A ]
deAminoABase 'F' = [ U , U , U ]
deAminoABase 'G' = [ G , G , U ]
deAminoABase 'H' = [ C , A , U ]
deAminoABase 'I' = [ A , U , U ]
deAminoABase 'K' = [ U , U , A ]
deAminoABase 'L' = [ C , U , U ]
deAminoABase 'M' = [ A , U , G ]
deAminoABase 'N' = [ A , A , U ]
deAminoABase 'P' = [ C , C , U ]
deAminoABase 'Q' = [ C , A , A ]
deAminoABase 'R' = [ A , G , A ]
deAminoABase 'S' = [ A , G , U ]
deAminoABase 'T' = [ A , C , U ]
deAminoABase 'V' = [ G , U , U ]
deAminoABase 'W' = [ U , G , G ]
deAminoABase 'Y' = [ G , U , U ]
deAminoABase e = error "No es un Aminoacido"


-- ## Reto 3 ## --
buscarTATAS :: String -> [String]
buscarTATAS "" = []
buscarTATAS s = sacarVacio( buscarTATA s : buscarTATAS (drop (length (buscarTATA s) + 4) s ))

buscarTATA :: String -> String
buscarTATA "" = error "No hay Cadena"
buscarTATA ('T' : 'A' : 'T' : 'A' : 'A' :'A' : ss) = case ss of 
                                               "" -> ""
                                               xs -> cortarEnTATA ss

buscarTATA ( s: ss) = buscarTATA ss

sacarVacio :: [String] -> [String]
sacarVacio [] = []
sacarVacio (x:xs) = case x of
                        "" -> []
                        x -> x : sacarVacio xs

cortarEnTATA :: String -> String
cortarEnTATA "" = error "No hay TATA final"
cortarEnTATA ('T' : 'A' : 'T' : 'A' :'A' : 'A' : ss) = ""
cortarEnTATA (s:ss) = s : cortarEnTATA ss 