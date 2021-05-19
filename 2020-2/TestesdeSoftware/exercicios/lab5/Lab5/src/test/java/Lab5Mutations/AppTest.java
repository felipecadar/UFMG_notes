package Lab5Mutations;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.Before;


public class AppTest 
{

    private App app;

    @Before
    public void setUp() {
        app = new App();
    }

    @Test
    public void testBigger()
    {
        Boolean r = app.isBigger(2, 1);
        assertTrue("1 > 2", r);
    }
}
