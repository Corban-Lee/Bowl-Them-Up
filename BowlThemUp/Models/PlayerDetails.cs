using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BowlThemUp.Models
{
    public class PlayerDetails
    {
        public int PlayerID { get; set; }
        public string FirstName { get; set; }
        public string Surname { get; set; }
        public int ShoeSize { get; set; }
        public int BallSize { get; set; }

        public virtual ICollection<BookingDetails>BookingDetails { get; set; }
    }
}
