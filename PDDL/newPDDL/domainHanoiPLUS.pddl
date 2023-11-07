(define (domain hanoiPLUS)

(:requirements
    :equality
    :negative-preconditions
    :numeric-fluents
    ;:object-fluents
    :typing
    :disjunctive-preconditions
    :conditional-effects
)

(:types
    disk 
    rod
    hand

)

(:predicates
    (smaller ?d1 ?d2 - disk)
    (equal ?d1 ?d2 - disk)
    
    (clear ?d - disk) ;d has no disks over it
        
    (on ?d1 - disk ?d2 - disk) ;d1 is on d2
        ;when  (on ?d1 - disk ?d2 - disk) is true, (clear ?d - disk) has to be false

    ;(empty ?r - rod) ;true if rod r has no disks on it
    (located ?d - disk ?r - rod);true if disk d is on rod r

    (handfull ?h - hand)

    (toAllocate ?d - disk)

)

(:functions
    (disks_number ?r - rod)
)

(:action take_block_conditional
    :parameters (?d1 - disk ?h - hand)
    :precondition (and 
        (not(handfull ?h))
        (clear ?d1)
    )

    :effect (and 
        (forall (?r - rod) 
            (when (located ?d1 ?r) 
                (and
                    (decrease (disks_number ?r) 1)
                    (not(located ?d1 ?r))
                )
            )
            ;per ogni rod del problema, se d1 e sul rod allora riduci il numero di dischi del rod.
        )        
        
        (forall (?d2 - disk) 
            (when (on ?d1 ?d2) 
                (and
                    (clear ?d2)
                    (not (on ?d1 ?d2))        
                )    
            )
        )

        (toAllocate ?d1)
        (handfull ?h)
    )
)


(:action put_block_on_block
    :parameters (?d1 ?d2 - disk  ?to - rod ?h - hand)
    :precondition (and 
        (>=(disks_number ?to)1)
        (or (equal ?d1 ?d2 ) (smaller ?d1 ?d2) )
        
        (handfull ?h)
        (toAllocate ?d1)
        (located ?d2 ?to)
        (clear ?d2)
     
    )
    :effect (and 
        (increase (disks_number ?to) 1)
        (located ?d1 ?to)
        (located ?d2 ?to)
        
        (not(clear ?d2))
        (clear ?d1)
        (on ?d1 ?d2)
        
        (not(handfull ?h))
        (not(toAllocate ?d1))
    )
)

(:action put_block_on_empty
    :parameters (?d1 - disk  ?to - rod ?h - hand)
    :precondition (and     
        (handfull ?h)
        (toAllocate ?d1)
        (= (disks_number ?to)0)
    )
    :effect (and            
        (increase (disks_number ?to) 1)
        (located ?d1 ?to)
        (clear ?d1)

        (not(toAllocate ?d1))
        (not(handfull ?h))

    )
)
 

)