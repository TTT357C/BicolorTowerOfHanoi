(define (problem move_r3_to_goal) (:domain hanoiPLUS)
(:objects
	w1 w2 w3 r1 r2 r3 - disk
	rod1 rod2 rod3 rod4 rod5 - rod
	h - hand
)
(:init
	(clear r1) (clear w1) 
	(located w1 rod1) (located r2 rod1) (located w3 rod1) 
	(located r1 rod2) (located w2 rod2) (located r3 rod2) 
	(=(disks_number rod1)3) (=(disks_number rod2)3) 
	(=(disks_number rod3)0) (=(disks_number rod4)0) (=(disks_number rod5)0) 

	(on w1 r2)(on r2 w3)
	(on r1 w2)(on w2 r3)

	(smaller w1 r2)(smaller w1 w2)(smaller w1 r3)(smaller w1 w3)
	(smaller r1 w2)(smaller r1 r2)(smaller r1 w3)(smaller r1 r3)
	(smaller w2 r3)(smaller w2 w3)
	(smaller r2 w3)(smaller r2 r3)
	
	(equal w1 r1)(equal r1 w1)
	(equal w2 r2)(equal r2 w2)
	(equal w3 r3)(equal r3 w3)
)
(:goal (and
	(located r1 rod1) (located r2 rod1) (located r3 rod1) 
	(located w1 rod2) (located w2 rod2) (located w3 rod2) 


	(=(disks_number rod1)3) (=(disks_number rod2)3) 
	(=(disks_number rod3)0) (=(disks_number rod4)0) (=(disks_number rod5)0) 
	(clear r1) 
	(clear w1) 
	(not(clear r2)) (not(clear r3)) 
	(not(clear w2)) (not(clear w3)) 
	
	(on r1 r2) (on r2 r3) 
	(on w1 w2) (on w2 w3) 
	(not(handfull h))
	(forall (?d - disk) (not(toAllocate ?d)) )
))
)