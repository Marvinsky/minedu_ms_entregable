package com.minedu.usi.msusi.repository;

import com.minedu.usi.msusi.model.TeacherObject;
import org.socialsignin.spring.data.dynamodb.repository.EnableScan;
import org.springframework.data.repository.CrudRepository;

@EnableScan
public interface TeacherObjectRepository extends CrudRepository<TeacherObject, String> {

}
