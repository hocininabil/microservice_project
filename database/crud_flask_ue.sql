
-- Database: `crud_flask_ue`
--

-- --------------------------------------------------------

--
-- Table structure for table `ue`
--

CREATE TABLE IF NOT EXISTS `ue` (
  `id` int(5) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `description` varchar(220) NOT NULL,
  `responsable` varchar(15) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

--
-- Insert table `ue`
--

INSERT INTO `ue` (`id`, `nom`, `description`, `responsable`) VALUES
(01, 'Programmation Web', 'xxxxxxaaaaa', 'nabil'),
(02, ' Systèmes information avancés 2', 'xxxxxxaaaaa', 'olivier');



--

--

--
ALTER TABLE `ue`
  ADD PRIMARY KEY (`id`);


--
ALTER TABLE `ue`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=21;

