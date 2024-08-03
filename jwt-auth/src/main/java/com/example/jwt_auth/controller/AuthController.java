package com.example.jwtauth.controller;

import com.example.jwtauth.model.AuthRequest;
import com.example.jwtauth.model.AuthResponse;
import com.example.jwtauth.util.JwtTokenUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/authenticate")
public class AuthController {

    @Autowired
    private AuthenticationManager authenticationManager;

    @Autowired
    private JwtTokenUtil jwtTokenUtil;

    @Autowired
    private MyUserDetailsService userDetailsService;

    @PostMapping
    public AuthResponse createAuthenticationToken(@RequestBody AuthRequest authRequest) throws Exception {
        try {
            authenticationManager.authenticate(
                    new UsernamePasswordAuthenticationToken(authRequest.getUsername(), authRequest.getPassword())
            );
        } catch (AuthenticationException e) {
            throw new Exception("Incorrect username or password", e);
        }

        final UserDetails userDetails = userDetailsService
                .loadUserByUsername(authRequest.getUsername());

        final String jwt = jwtTokenUtil.generateToken(userDetails.getUsername());

        return new AuthResponse(jwt);
    }
}

@Service
class MyUserDetailsService implements UserDetailsService {

    private static final String HARDCODED_USERNAME = "user";
    private static final String HARDCODED_PASSWORD = new BCryptPasswordEncoder().encode("password"); // hashed password

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        if (HARDCODED_USERNAME.equals(username)) {
            return User.builder()
                    .username(HARDCODED_USERNAME)
                    .password(HARDCODED_PASSWORD)
                    .roles("USER")
                    .build();
        } else {
            throw new UsernameNotFoundException("User not found");
        }
    }
}

