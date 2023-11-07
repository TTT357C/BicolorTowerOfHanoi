(define (problem two_diskPLUSHalfm2) (:domain hanoiPLUS)
(:objects
	r2 w1 w2 - disk
	rod1 rod2 rod3 - rod
	h - hand
)
(:init
	(clear w2) (clear w1) 
	(located w1 rod1) (located r2 rod1)
	(located w2 rod2)

	(=(disks_number rod1)2) (=(disks_number rod2)1) 
	(=(disks_number rod3)0) 

	(on w1 r2)

	(smaller w1 w2)(smaller w1 r2)	
	(equal r2 w2)(equal w2 r2)
)
(:goal (and
	 
	(located r2 rod3) 
	(located w1 rod2)  (located w2 rod2) 
	  
	(clear r2) 
	(clear w1)
	(not(clear w2)) 
	
	(on w1 w2) 

	(=(disks_number rod1)0) (=(disks_number rod2)2) 
	(=(disks_number rod3)1)
	 
	(not(handfull h))	
	(forall (?d - disk) (not(toAllocate ?d)) )
))
)