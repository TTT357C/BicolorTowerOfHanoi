(define (problem two_diskPLUSHalf) (:domain hanoiPLUS)
(:objects
	r1 r2 w1 w2 - disk
	rod1 rod2 rod3 - rod
	h - hand
)
(:init
	
	(located w1 rod1) (located r2 rod1) 
	(located r1 rod2) (located w2 rod2) 
	
	(clear w1) (clear r1) 

	(on w1 r2) (on r1 w2)

	(=(disks_number rod1)2) (=(disks_number rod2)2) (=(disks_number rod3)0) 

	(smaller r1 w2)(smaller r1 r2)
	(smaller w1 w2)(smaller w1 r2)
	
	(equal r1 w1)(equal w1 r1)
	(equal r2 w2)(equal w2 r2)
)
(:goal (and
	 
	(located r1 rod1)  (located r2 rod1) 
	(located w1 rod2)  (located w2 rod2) 

	(not(clear r2)) 
	(clear w1)
	(clear r1) 
	(not(clear w2)) 
	
	(on r1 r2)(on w1 w2) 
	
	(=(disks_number rod1)2) (=(disks_number rod2)2) (=(disks_number rod3)0)
	
	(not(handfull h))	
	(forall (?d - disk) (not(toAllocate ?d)) )
))
)