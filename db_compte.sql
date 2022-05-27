-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  lun. 23 mai 2022 à 10:33
-- Version du serveur :  10.4.6-MariaDB
-- Version de PHP :  7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `db_compte`
--

-- --------------------------------------------------------

--
-- Structure de la table `admin`
--

CREATE TABLE `admin` (
  `ID` int(11) NOT NULL,
  `USERNAME` char(25) NOT NULL,
  `PASSWORD` char(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `client`
--

CREATE TABLE `client` (
  `ID` int(11) NOT NULL,
  `CODE` char(25) NOT NULL,
  `NOM` char(25) NOT NULL,
  `POSTNOM` char(25) NOT NULL,
  `ADRESSE` text NOT NULL,
  `TELEPHONE` char(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `client`
--

INSERT INTO `client` (`ID`, `CODE`, `NOM`, `POSTNOM`, `ADRESSE`, `TELEPHONE`) VALUES
(1, '0001CB', 'Gilbert', 'kafunda', 'Golf plateau, c/ annexe, lubumbashi', '09785236254'),
(2, '0002CB', 'Kasongo', 'Kabalo', 'Golf plateau, c/ annexe, lubumbashi', '09785236789'),
(3, '0003CB', 'KASONGO', 'KASONGO', 'KASONGO', 'KASONGO'),
(4, '', '', '', '', ''),
(5, '1234', 'KIKULA', 'KIKULA', 'KIKULA', 'KIKULA'),
(6, '0005CB01', 'BUNTU', 'ISRAEL', 'kamalondo, shindaika', '0972542288');

-- --------------------------------------------------------

--
-- Structure de la table `compte`
--

CREATE TABLE `compte` (
  `ID` int(11) NOT NULL,
  `CODE` char(25) NOT NULL,
  `SOLDE` float NOT NULL,
  `DATE_CREATION` varchar(20) NOT NULL,
  `TITULAIRE` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `compte`
--

INSERT INTO `compte` (`ID`, `CODE`, `SOLDE`, `DATE_CREATION`, `TITULAIRE`) VALUES
(1, '0001CB01C', 30000, '02/05/2022 22:46', 1),
(2, '0002CB01C', 30000, '02/05/2022 22:46', 2),
(5, '0005CB01C', 30000, '22/05/2022 08:56', 5);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `compte`
--
ALTER TABLE `compte`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `TITULAIRE` (`TITULAIRE`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `admin`
--
ALTER TABLE `admin`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `client`
--
ALTER TABLE `client`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `compte`
--
ALTER TABLE `compte`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `compte`
--
ALTER TABLE `compte`
  ADD CONSTRAINT `compte_ibfk_1` FOREIGN KEY (`TITULAIRE`) REFERENCES `client` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
