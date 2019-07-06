-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Client :  127.0.0.1
-- Généré le :  Ven 31 Août 2018 à 13:31
-- Version du serveur :  10.1.10-MariaDB
-- Version de PHP :  5.6.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `hablo`
--

-- --------------------------------------------------------

--
-- Structure de la table `alert`
--

CREATE TABLE `alert` (
  `id` int(11) NOT NULL,
  `description` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Contenu de la table `alert`
--

INSERT INTO `alert` (`id`, `description`) VALUES
(1, 'your baby is feeling Hungry'),
(2, 'your baby is feeling Hungry');

-- --------------------------------------------------------

--
-- Structure de la table `baby`
--

CREATE TABLE `baby` (
  `id` int(11) NOT NULL,
  `gender` tinyint(1) NOT NULL,
  `birthDate` date NOT NULL,
  `inscriDate` date NOT NULL,
  `customer_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Contenu de la table `baby`
--

INSERT INTO `baby` (`id`, `gender`, `birthDate`, `inscriDate`, `customer_id`) VALUES
(5, 1, '2018-09-10', '2018-08-02', 1),
(2052277, 1, '2018-08-08', '2018-08-07', 1),
(3170314, 0, '2018-08-08', '2018-08-10', 1),
(3783056, 1, '2018-08-08', '2018-08-08', 1);

-- --------------------------------------------------------

--
-- Structure de la table `cry`
--

CREATE TABLE `cry` (
  `id` int(11) NOT NULL,
  `fileName` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `srcAudioFile` varchar(200) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `customer`
--

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `lastname` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `birthDate` date NOT NULL,
  `email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `adresse` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `login` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `pwd` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `srcImg` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `altImg` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `inscripDate` date NOT NULL,
  `active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Contenu de la table `customer`
--

INSERT INTO `customer` (`id`, `name`, `lastname`, `birthDate`, `email`, `phone`, `adresse`, `login`, `pwd`, `srcImg`, `altImg`, `inscripDate`, `active`) VALUES
(1, 'Aligggg', 'ben aliggggg', '1980-08-01', 'alibensliman14@gmail.com', '53750443', 'dddd', '123', '123', 'http://10.68.11.61/ProjectApi/api/Images/customer/idCust147852/idCust147852_Dessinclasses.jpg', 'null', '2018-08-01', 1);

-- --------------------------------------------------------

--
-- Structure de la table `customer_alert`
--

CREATE TABLE `customer_alert` (
  `id` int(11) NOT NULL,
  `alertDate` date NOT NULL,
  `seen` tinyint(1) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `alert_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Contenu de la table `customer_alert`
--

INSERT INTO `customer_alert` (`id`, `alertDate`, `seen`, `customer_id`, `alert_id`) VALUES
(1, '2018-07-04', 0, 1, 1),
(2, '2018-08-01', 1, 1, 2),
(3, '2018-08-14', 1, 1, 1),
(4, '2018-08-08', 0, 1, 1),
(5, '2018-08-06', 0, 1, 2),
(6, '2018-08-15', 1, 1, 1),
(7, '2018-08-14', 0, 1, 2),
(8, '2018-08-14', 0, 1, 2),
(9, '2018-08-06', 1, 1, 2);

-- --------------------------------------------------------

--
-- Structure de la table `device`
--

CREATE TABLE `device` (
  `id` int(11) NOT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `active` tinyint(1) NOT NULL,
  `inscriDate` date NOT NULL,
  `token` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `customer_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Contenu de la table `device`
--

INSERT INTO `device` (`id`, `name`, `active`, `inscriDate`, `token`, `customer_id`) VALUES
(1, 'hablo', 1, '2018-08-07', 'ABCD', 1);

-- --------------------------------------------------------

--
-- Structure de la table `device_cry`
--

CREATE TABLE `device_cry` (
  `id` int(11) NOT NULL,
  `cryDate` date NOT NULL,
  `status` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `device_id` int(11) DEFAULT NULL,
  `cry_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `disease`
--

CREATE TABLE `disease` (
  `id` int(11) NOT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `doctor`
--

CREATE TABLE `doctor` (
  `id` int(11) NOT NULL,
  `name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `lastname` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `birthDate` date NOT NULL,
  `srcImg` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `altImg` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `active` tinyint(1) NOT NULL,
  `phone` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `cellphone` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `street` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `city` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `state` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `doctors_diseases`
--

CREATE TABLE `doctors_diseases` (
  `doctor_id` int(11) NOT NULL,
  `disease_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `phone`
--

CREATE TABLE `phone` (
  `id` int(11) NOT NULL,
  `token` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `customer_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Contenu de la table `phone`
--

INSERT INTO `phone` (`id`, `token`, `customer_id`) VALUES
(4, 'aaf422db1d080d02', 1),
(7, 'eIJb8TK6l9c:APA91bHHtdPpRL0uMmwm0W2dWjUjKF3Hu7M9WTcv7MQdDz656KP3tua1FihBwoMuFCVQFzKOnh1_Vi9HgQfOZSxp', 1),
(8, 'eIJb8TK6l9c:APA91bHHtdPpRL0uMmwm0W2dWjUjKF3Hu7M9WTcv7MQdDz656KP3tua1FihBwoMuFCVQFzKOnh1_Vi9HgQfOZSxp', 1),
(9, 'eIJb8TK6l9c:APA91bHHtdPpRL0uMmwm0W2dWjUjKF3Hu7M9WTcv7MQdDz656KP3tua1FihBwoMuFCVQFzKOnh1_Vi9HgQfOZSxp5xFddbL7shGNuDIHT84GEOxXkdm0abeDKQe3G9etriYEcXHYfRpT', 1),
(10, 'cDw7sJNTWR0:APA91bEq6BNsPuA9g_DRHCQSG89O5aXw0Vvdp1fSwJiGQC-FvDd36tsKfFLkCcCHRpH3ZE2wMjUl_VWRG2-KmXf8wx4FCiimqSg2AhN4AueCmkV_FiOhtRFSDxjpio3fgXznd5eQvEV0', 1),
(11, 'eU3O7PrmoDw:APA91bE7gLqxQBf7oLLXx-WMD5vX1RrHJzLniNMpDErx0p4XbgOwnqOg4tvxNmKETtUIoAnLer7dDviHTM-LazSXQDoMcmhfJe75Ft4VOpdLciOJPgyoDfGSnqRAtqYF8v04v293rAX8', 1),
(12, 'c0st-5ZTcRQ:APA91bErMFqNeZnRzPRlfgqmhy0EXxG_tp9jMoEzCiiLzokEjUdAy3O8-SrpOPQei-bawNVkimNmKQKz04So8_zZSAZEStfyw2YceNrpbrXeV8EKbbW1_iF6D0fPjXnJzs3IaUDvVqjY', 1),
(13, 'f5iM2JOlclI:APA91bH9qYd9mD3-FSvg3WGPhd6YKOSn3Jw9gf1_tb9Sv_XtKT0w1-Zf8sFZMoqFv3NqTAzh5mur7gz3Z93z3S26fCnhBM11fWmS8V-ljs-yEcfsEFA929J90PYi2WCB5-UlaJE_CFll', 1);

-- --------------------------------------------------------

--
-- Structure de la table `symptoms`
--

CREATE TABLE `symptoms` (
  `id` int(11) NOT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `symptomsbabies`
--

CREATE TABLE `symptomsbabies` (
  `id` int(11) NOT NULL,
  `dateSymptoms` date NOT NULL,
  `description` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `symptoms_id` int(11) DEFAULT NULL,
  `baby_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `symptoms_diseases`
--

CREATE TABLE `symptoms_diseases` (
  `disease_id` int(11) NOT NULL,
  `symptoms_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Index pour les tables exportées
--

--
-- Index pour la table `alert`
--
ALTER TABLE `alert`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `baby`
--
ALTER TABLE `baby`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IDX_876C813E9395C3F3` (`customer_id`);

--
-- Index pour la table `cry`
--
ALTER TABLE `cry`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `customer_alert`
--
ALTER TABLE `customer_alert`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IDX_D9C833FA9395C3F3` (`customer_id`),
  ADD KEY `IDX_D9C833FA93035F72` (`alert_id`);

--
-- Index pour la table `device`
--
ALTER TABLE `device`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IDX_92FB68E9395C3F3` (`customer_id`);

--
-- Index pour la table `device_cry`
--
ALTER TABLE `device_cry`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IDX_6BFEA41E94A4C7D4` (`device_id`),
  ADD KEY `IDX_6BFEA41E33879CCC` (`cry_id`);

--
-- Index pour la table `disease`
--
ALTER TABLE `disease`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `doctors_diseases`
--
ALTER TABLE `doctors_diseases`
  ADD PRIMARY KEY (`doctor_id`,`disease_id`),
  ADD KEY `IDX_43D1C19287F4FB17` (`doctor_id`),
  ADD KEY `IDX_43D1C192D8355341` (`disease_id`);

--
-- Index pour la table `phone`
--
ALTER TABLE `phone`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IDX_444F97DD9395C3F3` (`customer_id`);

--
-- Index pour la table `symptoms`
--
ALTER TABLE `symptoms`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `symptomsbabies`
--
ALTER TABLE `symptomsbabies`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IDX_3EDC328467CA3534` (`symptoms_id`),
  ADD KEY `IDX_3EDC32842E288954` (`baby_id`);

--
-- Index pour la table `symptoms_diseases`
--
ALTER TABLE `symptoms_diseases`
  ADD PRIMARY KEY (`disease_id`,`symptoms_id`),
  ADD KEY `IDX_319D0A61D8355341` (`disease_id`),
  ADD KEY `IDX_319D0A6167CA3534` (`symptoms_id`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `alert`
--
ALTER TABLE `alert`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT pour la table `baby`
--
ALTER TABLE `baby`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3783057;
--
-- AUTO_INCREMENT pour la table `cry`
--
ALTER TABLE `cry`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT pour la table `customer_alert`
--
ALTER TABLE `customer_alert`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT pour la table `device`
--
ALTER TABLE `device`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT pour la table `device_cry`
--
ALTER TABLE `device_cry`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `disease`
--
ALTER TABLE `disease`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `doctor`
--
ALTER TABLE `doctor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `phone`
--
ALTER TABLE `phone`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT pour la table `symptoms`
--
ALTER TABLE `symptoms`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `symptomsbabies`
--
ALTER TABLE `symptomsbabies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `baby`
--
ALTER TABLE `baby`
  ADD CONSTRAINT `FK_876C813E9395C3F3` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`);

--
-- Contraintes pour la table `customer_alert`
--
ALTER TABLE `customer_alert`
  ADD CONSTRAINT `FK_D9C833FA93035F72` FOREIGN KEY (`alert_id`) REFERENCES `alert` (`id`),
  ADD CONSTRAINT `FK_D9C833FA9395C3F3` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`);

--
-- Contraintes pour la table `device`
--
ALTER TABLE `device`
  ADD CONSTRAINT `FK_92FB68E9395C3F3` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`);

--
-- Contraintes pour la table `device_cry`
--
ALTER TABLE `device_cry`
  ADD CONSTRAINT `FK_6BFEA41E33879CCC` FOREIGN KEY (`cry_id`) REFERENCES `cry` (`id`),
  ADD CONSTRAINT `FK_6BFEA41E94A4C7D4` FOREIGN KEY (`device_id`) REFERENCES `device` (`id`);

--
-- Contraintes pour la table `doctors_diseases`
--
ALTER TABLE `doctors_diseases`
  ADD CONSTRAINT `FK_43D1C19287F4FB17` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `FK_43D1C192D8355341` FOREIGN KEY (`disease_id`) REFERENCES `disease` (`id`) ON DELETE CASCADE;

--
-- Contraintes pour la table `symptomsbabies`
--
ALTER TABLE `symptomsbabies`
  ADD CONSTRAINT `FK_3EDC32842E288954` FOREIGN KEY (`baby_id`) REFERENCES `baby` (`id`),
  ADD CONSTRAINT `FK_3EDC328467CA3534` FOREIGN KEY (`symptoms_id`) REFERENCES `symptoms` (`id`);

--
-- Contraintes pour la table `symptoms_diseases`
--
ALTER TABLE `symptoms_diseases`
  ADD CONSTRAINT `FK_319D0A6167CA3534` FOREIGN KEY (`symptoms_id`) REFERENCES `symptoms` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `FK_319D0A61D8355341` FOREIGN KEY (`disease_id`) REFERENCES `disease` (`id`) ON DELETE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
