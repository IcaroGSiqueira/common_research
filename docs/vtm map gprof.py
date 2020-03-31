\[\d+\][ \d \.]+[A-Za-z]+::compressGOP
	\[\d+\][ \d \.]+[A-Za-z]+::compressSlice
		\[\d+\][ \d \.]+[A-Za-z]+::encodeCtus
			\[\d+\][ \d \.]+[A-Za-z]+::compressCtu
				\[\d+\][ \d \.]+[A-Za-z]+::xCompressCU
					\[\d+\][ \d \.]+[A-Za-z]+::xCheckRDCostMerge2Nx2N
					\[\d+\][ \d \.]+[A-Za-z]+::xCheckRDCostInterIMV
					\[\d+\][ \d \.]+[A-Za-z]+::xCheckRDCostInter
					\[\d+\][ \d \.]+[A-Za-z]+::xCheckRDCostIntra
					\[\d+\][ \d \.]+[A-Za-z]+::xCheckRDCostMergeTriangle2Nx2N
					\[\d+\][ \d \.]+[A-Za-z]+::xCheckRDCostAffineMerge2Nx2N

						\[\d+\][ \d \.]+[A-Za-z]+::xEncodeInterResidual
							\[\d+\][ \d \.]+[A-Za-z]+::encodeResAndCalcRdInterCU
								\[\d+\][ \d \.]+[A-Za-z]+::xEstimateInterResidualQT
									\[\d+\][ \d \.]+[A-Za-z]+::TrQuant::transformNxN
									\[\d+\][ \d \.]+[A-Za-z]+::residual_coding

	\[\d+\][ \d \.]+[A-Za-z]+::ALFProcess
		\[\d+\][ \d \.]+[A-Za-z]+::alfEncoder
			\[\d+\][ \d \.]+[A-Za-z]+::getFilterCoeffAndCost
				\[\d+\][ \d \.]+[A-Za-z]+::mergeFiltersAndCost
					\[\d+\][ \d \.]+[A-Za-z]+::mergeClasses
						\[\d+\][ \d \.]+[A-Za-z]+::optimizeFilterClip
							\[\d+\][ \d \.]+[A-Za-z]+::optimizeFilter
								\[\d+\][ \d \.]+[A-Za-z]+::gnsSolveByChol
					\[\d+\][ \d \.]+[A-Za-z]+::deriveFilterCoeffs
						\[\d+\][ \d \.]+[A-Za-z]+::deriveCoeffQuant
							\[\d+\][ \d \.]+[A-Za-z]+::optimizeFilter
								\[\d+\][ \d \.]+[A-Za-z]+::gnsSolveByChol					
		\[\d+\][ \d \.]+[A-Za-z]+::alfEncoderCtb

		\[\d+\][ \d \.]+[A-Za-z]+::deriveStatsForFiltering

			\[\d+\][ \d \.]+[A-Za-z]+::getBlkStats
				\[\d+\][ \d \.]+[A-Za-z]+::calcCovariance
					\[\d+\][ \d \.]+[A-Za-z]+::clipALF